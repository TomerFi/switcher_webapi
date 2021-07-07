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

"""Rest service implemented with aiohttp for integrating the Switcher smart devices."""

import logging
from argparse import ArgumentParser
from datetime import timedelta
from enum import Enum
from typing import Callable, Dict, List, Set, Union

from aiohttp import web
from aioswitcher.api import Command, SwitcherApi
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

ENDPOINT_GET_STATE = "/switcher/get_state"
ENDPOINT_TURN_ON = "/switcher/turn_on"
ENDPOINT_TURN_OFF = "/switcher/turn_off"
ENDPOINT_SET_AUTO_SHUTDOWN = "/switcher/set_auto_shutdown"
ENDPOINT_SET_NAME = "/switcher/set_name"
ENDPOINT_GET_SCHEDULES = "/switcher/get_schedules"
ENDPOINT_DELETE_SCHEDULE = "/switcher/delete_schedule"
ENDPOINT_CREATE_SCHEDULE = "/switcher/create_schedule"

log_level_dict = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

parser = ArgumentParser(
    description="Start an aiohttp rest service integrating with Switcher devices."
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
    choices=list(log_level_dict.keys()),
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


@web.middleware
async def error_middleware(request: web.Request, handler: Callable) -> web.Response:
    """Middleware for handling server exceptions."""
    try:
        return await handler(request)
    except Exception as exc:
        logging.exception("caught exception while handing over to endpoint")
        return web.json_response({"error": str(exc)}, status=500)


if __name__ == "__main__":
    args = parser.parse_args()

    app = web.Application(middlewares=[error_middleware])
    logging.basicConfig(level=log_level_dict[args.log_level])
    app.add_routes(routes)

    web.run_app(app, port=args.port)
