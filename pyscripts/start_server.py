"""Sanic server for the Switcher WebAPI."""

from argparse import ArgumentParser
from asyncio import AbstractEventLoop, get_event_loop, set_event_loop
from functools import partial, update_wrapper
from sys import exit as sys_exit
from typing import Optional

from asyncio_throttle import Throttler
from sanic import Sanic
from sanic.exceptions import SanicException, ServerError
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, text
from uvloop import new_event_loop

import mappings
from request_handlers import (create_schedule_handler, delete_schedule_handler,
                              disable_schedule_handler,
                              enable_schedule_handler, get_schedules_handler,
                              get_state_handler, set_auto_shutdown_handler,
                              set_device_name_handler, turn_off_handler,
                              turn_on_handler)

CONF_PHONE_ID = 'PHONE_ID'
CONF_DEVICE_ID = 'DEVICE_ID'
CONF_DEVICE_PASSWORD = 'DEVICE_PASSWORD'  # nosec
CONF_DEVICE_IP_ADDR = 'DEVICE_IP_ADDR'
CONF_THROTTLE = 'THROTTLE'

# pylint: disable=invalid-name
sanic_app = Sanic(__name__, load_env='CONF_')
# pylint: enable=invalid-name


def _wrapped_partial(func, *args, **kwargs):
    """Use as wrapper for updating __name__ for partial."""
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func

# pylint: disable=unused-argument
@sanic_app.listener('before_server_start')
def before_start(app: Sanic, loop: AbstractEventLoop) -> None:
    """Use for preparing data and register mappings before start."""
    app.config[CONF_PHONE_ID] = (
        '0000{}'.format(app.config[CONF_PHONE_ID]))[-4:]
    app.config[CONF_DEVICE_ID] = (
        '000000{}'.format(app.config[CONF_DEVICE_ID]))[-6:]
    app.config[CONF_DEVICE_PASSWORD] = (
        '00000000{}'.format(app.config[CONF_DEVICE_PASSWORD]))[-8:]
    app.config[CONF_THROTTLE] = float(app.config[CONF_THROTTLE]) \
        if CONF_THROTTLE in app.config else 5.0

    app.config.REQUEST_TIMEOUT = 10
    app.config.RESPONSE_TIMEOUT = 10
    app.config.GRACEFUL_SHUTDOWN_TIMEOUT = 10

    request_throttler = Throttler(
        rate_limit=1, period=app.config[CONF_THROTTLE])

    # pylint: disable=unused-variable
    @app.middleware('request')
    async def requests_middleware(request: Request) -> None:
        """Use for aquiring a throttle as a middleware for all requests."""
        await request_throttler.acquire()
    # pylint: enable=unused-variable

    kwargs_dict = {
        'ip_address': app.config[CONF_DEVICE_IP_ADDR],
        'phone_id': app.config[CONF_PHONE_ID],
        'device_id': app.config[CONF_DEVICE_ID],
        'device_password': app.config[CONF_DEVICE_PASSWORD]
    }

    app.add_route(_wrapped_partial(get_state_handler, **kwargs_dict),
                  mappings.URL_MAPPING_GET_STATE, methods=['GET'])

    app.add_route(_wrapped_partial(turn_on_handler, **kwargs_dict),
                  mappings.URL_MAPPING_TURN_ON, methods=['POST'])

    app.add_route(_wrapped_partial(turn_off_handler, **kwargs_dict),
                  mappings.URL_MAPPING_TURN_OFF, methods=['POST'])

    app.add_route(_wrapped_partial(set_auto_shutdown_handler, **kwargs_dict),
                  mappings.URL_MAPPING_SET_AUTO_SHUTDOWN, methods=['POST'])

    app.add_route(_wrapped_partial(set_device_name_handler, **kwargs_dict),
                  mappings.URL_MAPPING_SET_DEVICE_NAME, methods=['POST'])

    app.add_route(_wrapped_partial(get_schedules_handler, **kwargs_dict),
                  mappings.URL_MAPPING_GET_SCHEDULES, methods=['GET'])

    app.add_route(_wrapped_partial(enable_schedule_handler, **kwargs_dict),
                  mappings.URL_MAPPING_ENABLE_SCHEDULE, methods=['PATCH'])

    app.add_route(_wrapped_partial(disable_schedule_handler, **kwargs_dict),
                  mappings.URL_MAPPING_DISABLE_SCHEDULE, methods=['PATCH'])

    app.add_route(_wrapped_partial(delete_schedule_handler, **kwargs_dict),
                  mappings.URL_MAPPING_DELETE_SCHEDULE, methods=['DELETE'])

    app.add_route(_wrapped_partial(create_schedule_handler, **kwargs_dict),
                  mappings.URL_MAPPING_CREATE_SCHEDULE, methods=['PUT'])


@sanic_app.exception(ServerError)
def timeout(request: Request, exception: SanicException) -> HTTPResponse:
    """Use as custom handler for logging internal service errors."""
    logger.error(exception)
    return text('Internal service failure, please check logs.', 500)
# pylint: enable=unused-argument


if __name__ == '__main__':
    # pylint: disable=invalid-name
    parser = ArgumentParser(
        description="Start asynchronous Switcher web api with Sanic.")

    parser.add_argument(
        '-p', '--port', type=int, default=3698,
        help="port for the server to run on, default is 3698")

    set_event_loop(new_event_loop())
    server_coro = sanic_app.create_server(
        host='0.0.0.0', port=parser.parse_args().port,  # nosec
        return_asyncio_server=True)
    event_loop = None  # type: Optional[AbstractEventLoop]
    try:
        event_loop = get_event_loop()
        event_loop.create_task(server_coro)
        event_loop.run_forever()
        sanic_app.stop()
    except RuntimeError as exc:
        logger.error(exc)
    finally:
        if event_loop:
            event_loop.stop()
    sys_exit()
    # pylint: enable=invalid-name
