# Copyright Tomer Figenblat.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Web service implemented with aiohttp for integrating the Switcher smart devices."""

from argparse import ArgumentParser
from datetime import timedelta
from enum import Enum
from logging import config
from typing import Callable, Dict, List, Set, Union

from aiohttp import web
from aiohttp.abc import AbstractAccessLogger
from aiohttp.log import (
    access_logger,
    client_logger,
    server_logger,
    web_logger,
    ws_logger,
)
from aiohttp.web_request import BaseRequest
from aiohttp.web_response import StreamResponse
from aioswitcher.api import Command, SwitcherApi, SWITCHER_TCP_PORT_TYPE2
from aioswitcher.schedule import Days

KEY_ID = "id"
KEY_IP = "ip"
KEY_NAME = "name"
KEY_HOURS = "hours"
KEY_MINUTES = "minutes"
KEY_SCHEDULE = "schedule"
KEY_START = "start"
KEY_STOP = "stop"
KEY_DAYS = "days"
KEY_POSITION = "position"

ENDPOINT_GET_STATE = "/switcher/get_state"
ENDPOINT_TURN_ON = "/switcher/turn_on"
ENDPOINT_TURN_OFF = "/switcher/turn_off"
ENDPOINT_SET_AUTO_SHUTDOWN = "/switcher/set_auto_shutdown"
ENDPOINT_SET_NAME = "/switcher/set_name"
ENDPOINT_GET_SCHEDULES = "/switcher/get_schedules"
ENDPOINT_DELETE_SCHEDULE = "/switcher/delete_schedule"
ENDPOINT_CREATE_SCHEDULE = "/switcher/create_schedule"
ENDPOINT_SET_POSITION = "/switcher/set_position"

parser = ArgumentParser(
    description="Start an aiohttp web service integrating with Switcher devices."
)

parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=3698,
    help="port for the server to run on, default is 3698",
)

parser.add_argument(
    "-l",
    "--log-level",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    default="INFO",
    help="log level for reporting",
)

routes = web.RouteTableDef()


def _serialize_object(obj: object) -> Dict[str, Union[List[str], str]]:
    """Use for converting enum to primitives and remove not relevant keys ."""
    serialized_dict = dict()  # type: Dict[str, Union[List[str], str]]
    for k, v in obj.__dict__.items():
        if not k == "unparsed_response":
            if isinstance(v, Enum):
                serialized_dict[k] = v.name
            elif isinstance(v, Set):
                serialized_dict[k] = [m.name if isinstance(m, Enum) else m for m in v]
            else:
                serialized_dict[k] = v
    return serialized_dict


@routes.get(ENDPOINT_GET_STATE)
async def get_state(request: web.Request) -> web.Response:
    """Use to get the current state of the device."""
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(_serialize_object(await swapi.get_state()))


@routes.post(ENDPOINT_TURN_ON)
async def turn_on(request: web.Request) -> web.Response:
    """Use to turn on the device."""
    if request.body_exists:
        body = await request.json()
        minutes = int(body[KEY_MINUTES]) if body.get(KEY_MINUTES) else 0
    else:
        minutes = 0
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(
            _serialize_object(await swapi.control_device(Command.ON, minutes))
        )


@routes.post(ENDPOINT_TURN_OFF)
async def turn_off(request: web.Request) -> web.Response:
    """Use to turn on the device."""
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(
            _serialize_object(await swapi.control_device(Command.OFF))
        )


@routes.patch(ENDPOINT_SET_NAME)
async def set_name(request: web.Request) -> web.Response:
    """Use to set the device's name."""
    try:
        body = await request.json()
        name = body[KEY_NAME]
    except Exception as exc:
        raise ValueError(f"failed to get {KEY_NAME} from body as json") from exc
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(_serialize_object(await swapi.set_device_name(name)))


@routes.patch(ENDPOINT_SET_AUTO_SHUTDOWN)
async def set_auto_shutdown(request: web.Request) -> web.Response:
    """Use to set the device's auto shutdown configuration value."""
    try:
        body = await request.json()
        hours = body[KEY_HOURS]
        minutes = int(body[KEY_MINUTES]) if body.get(KEY_MINUTES) else 0
    except Exception as exc:
        raise ValueError("failed to get hours from body as json") from exc
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(
            _serialize_object(
                await swapi.set_auto_shutdown(
                    timedelta(hours=int(hours), minutes=int(minutes) if minutes else 0)
                )
            )
        )


@routes.get(ENDPOINT_GET_SCHEDULES)
async def get_schedules(request: web.Request) -> web.Response:
    """Use to get the current configured schedules on the device."""
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        response = await swapi.get_schedules()
        return web.json_response([_serialize_object(s) for s in response.schedules])


@routes.delete(ENDPOINT_DELETE_SCHEDULE)
async def delete_schedule(request: web.Request) -> web.Response:
    """Use to delete an existing schedule."""
    try:
        body = await request.json()
        schedule_id = body[KEY_SCHEDULE]
    except Exception as exc:
        raise ValueError("failed to get schedule from body as json") from exc
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(
            _serialize_object(await swapi.delete_schedule(schedule_id))
        )


@routes.post(ENDPOINT_CREATE_SCHEDULE)
async def create_schedule(request: web.Request) -> web.Response:
    """Use to create a new schedule."""
    weekdays = dict(map(lambda d: (d.value, d), Days))
    body = await request.json()
    start_time = body[KEY_START]
    stop_time = body[KEY_STOP]
    selected_days = (
        set([weekdays[d] for d in body[KEY_DAYS]]) if body.get(KEY_DAYS) else set()
    )
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID]) as swapi:
        return web.json_response(
            _serialize_object(
                await swapi.create_schedule(start_time, stop_time, selected_days)
            )
        )


@routes.post(ENDPOINT_SET_POSITION)
async def set_position(request: web.Request) -> web.Response:
    """Use for setting the shutter position of the Runner and Runner Mini devices."""
    try:
        position = int(request.query[KEY_POSITION])
    except Exception as exc:
        raise ValueError("failed to get position from body as json") from exc
    async with SwitcherApi(request.query[KEY_IP], request.query[KEY_ID], SWITCHER_TCP_PORT_TYPE2) as swapi:
        return web.json_response(
            _serialize_object(
                await swapi.set_position(position)
            )
        )



@web.middleware
async def error_middleware(request: web.Request, handler: Callable) -> web.Response:
    """Middleware for handling server exceptions."""
    try:
        return await handler(request)
    except Exception as exc:
        server_logger.exception("caught exception while handing over to endpoint")
        return web.json_response({"error": str(exc)}, status=500)


class CustomAccessLogger(AbstractAccessLogger):
    """Custom implementation of the aiohttp access logger."""

    def log(self, request: BaseRequest, response: StreamResponse, time: float) -> None:
        """Log as debug instead origin info."""
        remote = request.remote
        method = request.method
        path = request.path
        status = response.status
        self.logger.debug(f"{remote} {method} {path} done in {time}s: {status}")


if __name__ == "__main__":
    args = parser.parse_args()

    loggingConfig = {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "stream": {
                "formatter": "default",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "": {"handlers": ["stream"], "propagate": True},
            "aioswitcher.api": {"level": "WARNING"},
            access_logger.name: {"level": args.log_level},
            client_logger.name: {"level": args.log_level},
            server_logger.name: {"level": args.log_level},
            web_logger.name: {"level": args.log_level},
            ws_logger.name: {"level": args.log_level},
        },
    }

    config.dictConfig(loggingConfig)

    app = web.Application(middlewares=[error_middleware])
    app.add_routes(routes)

    server_logger.info("starting server")
    web.run_app(app, port=args.port, access_log_class=CustomAccessLogger)
    server_logger.info("server stopped")
