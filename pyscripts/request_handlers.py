"""Request handlers for the Switcher WebAPI."""

# fmt: off
from asyncio import get_running_loop
from datetime import timedelta
from typing import Dict, List, Optional

from aioswitcher.api import SwitcherV2Api, messages
from aioswitcher.consts import (COMMAND_OFF, COMMAND_ON, DAY_TO_INT_DICT,
                                DISABLE_SCHEDULE, ENABLE_SCHEDULE,
                                SCHEDULE_CREATE_DATA_FORMAT, WEEKDAY_TUP)
from aioswitcher.errors import CalculationError, DecodingError, EncodingError
from aioswitcher.schedules import calc_next_run_for_schedule
from aioswitcher.tools import (create_weekdays_value,
                               timedelta_str_to_schedule_time)
from sanic.exceptions import InvalidUsage, ServerError, ServiceUnavailable
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, json

import consts

# fmt: on

ExceptionSet = (CalculationError, DecodingError, EncodingError)


async def get_state_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling GET requests to /switcher/get_state.

    Returns a json object represnting the current state.
    """
    try:
        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.get_state()

        if not response:
            raise ServiceUnavailable("Failed to get response from api.", 503)

        await response.init_future
        state_response = response.init_future.result()

        if (
            state_response
            and state_response.successful
            and state_response.msg_type == messages.ResponseMessageType.STATE
        ):
            return json(
                {
                    consts.KEY_SUCCESSFUL: state_response.successful,
                    consts.KEY_STATE: state_response.state,
                    consts.KEY_TIME_LEFT: state_response.time_left,
                    consts.KEY_AUTO_OFF: state_response.auto_off,
                    consts.KEY_POWER_CONSUMPTION: state_response.power,
                    consts.KEY_ELECTRIC_CURRENT: state_response.current,
                }
            )
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed retrieving the device's state.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed to get the device state.", 500) from exc


async def turn_off_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling POST requests to /switcher/turn_off.

    Returns a json object represnting the request status.
    """
    try:
        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.control_device(COMMAND_OFF)

        if (
            response
            and response.msg_type == messages.ResponseMessageType.CONTROL
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed turning off the device.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed turning off the device.", 500) from exc


async def get_schedules_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling GET requests to /switcher/get_schedules.

    Returns a json object represnting the device's configured schedules.
    """
    try:
        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.get_schedules()

        if response and response.successful:
            schedules_list = []  # type: List[Dict]
            if response.found_schedules:
                for schedule in response.get_schedules:
                    await schedule.init_future
                    schedule_obj = schedule.init_future.result()
                    next_run = await calc_next_run_for_schedule(
                        get_running_loop(), schedule_obj
                    )
                    schedules_list.append(
                        {
                            consts.KEY_SCHEDULE_ID: schedule_obj.schedule_id,
                            consts.KEY_ENABLED: schedule_obj.enabled,
                            consts.KEY_RECURRING: schedule_obj.recurring,
                            consts.KEY_DAYS: schedule_obj.days,
                            consts.KEY_START_TIME: schedule_obj.start_time,
                            consts.KEY_END_TIME: schedule_obj.end_time,
                            consts.KEY_DURATION: schedule_obj.duration,
                            consts.KEY_SCHEDULE_DATA:
                                schedule_obj.schedule_data,
                            consts.KEY_NEXT_RUN: next_run,
                        }
                    )
            return json(
                {
                    consts.KEY_SUCCESSFUL: response.successful,
                    consts.KEY_FOUND_SCHEDULES: response.found_schedules,
                    consts.KEY_SCHEDULES: schedules_list,
                }
            )
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed getting the device schedules.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed to get the device schedules.", 500) from exc


async def turn_on_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling POST requests to /switcher/turn_on.

    Accepts minutes string param (1-180) in url or body, none for no timer.
    Returns a json object represnting the request status.
    """
    try:
        minutes = None  # type: Optional[str]
        if request.args and consts.PARAM_MINUTES in request.args:
            minutes = request.args[consts.PARAM_MINUTES][0]
        elif request.json and consts.PARAM_MINUTES in request.json:
            minutes = str(request.json[consts.PARAM_MINUTES])
        if minutes and (int(minutes) < 1 or int(minutes) > 180):
            logger.info("Invalid usage, timer requested is %s", minutes)
            raise InvalidUsage(
                "Can only accept timer for 1 to 180 minutes.", 400
            )
        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            if minutes:
                response = await swapi.control_device(COMMAND_ON, minutes)
            else:
                response = await swapi.control_device(COMMAND_ON)

        if (
            response
            and response.msg_type == messages.ResponseMessageType.CONTROL
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed turning on the device.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed turning on the device.", 500) from exc


async def set_auto_shutdown_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling POST requests to /switcher/set_auto_shutdown.

    Accepts hours and minutes as int arguments, total between 1 and 3 hours.
    Returns a json object represnting the request status.
    """
    try:
        if (
            request.args
            and consts.PARAM_HOURS in request.args
            and consts.PARAM_MINUTES in request.args
        ):
            hours = int(request.args[consts.PARAM_HOURS][0])
            minutes = int(request.args[consts.PARAM_MINUTES][0])
        elif (
            request.json
            and consts.PARAM_HOURS in request.json
            and consts.PARAM_MINUTES in request.json
        ):
            hours = int(request.json[consts.PARAM_HOURS])
            minutes = int(request.json[consts.PARAM_MINUTES])
        else:
            raise InvalidUsage(
                "One of the arguments hours or minutes is missing.", 400
            )

        time_guard = (hours * 60 if hours > 0 else 0) + (
            minutes if minutes > 0 else 0
        )
        if time_guard < 59 or time_guard > 180:
            raise InvalidUsage(
                "Auto shutdown can be set between 1 and 3 hours.", 400
            )

        time_to_off_timedelta = timedelta(hours=hours, minutes=minutes)

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.set_auto_shutdown(time_to_off_timedelta)

        if (
            response
            and response.msg_type == messages.ResponseMessageType.AUTO_OFF
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed setting auto shutdown on device.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError(
            "Failed setting auto shutdown on device.", 500
        ) from exc


async def set_device_name_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling POST requests to /switcher/set_device_name.

    Accepts name str with length between 2 and 32 in url or body.
    Returns a json object represnting the request status.
    """
    try:
        if request.args and consts.PARAM_NAME in request.args:
            name = request.args[consts.PARAM_NAME][0]
        elif request.json and consts.PARAM_NAME in request.json:
            name = str(request.json[consts.PARAM_NAME])
        else:
            raise InvalidUsage("Argument name is missing.", 400)
        if len(name) < 2 or len(name) > 32:
            raise InvalidUsage(
                "Only accepts name with length between 2 and 32.", 400
            )

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.set_device_name(name)

        if (
            response
            and response.msg_type == messages.ResponseMessageType.UPDATE_NAME
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed setting the device name.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed setting the device name.", 500) from exc


async def enable_schedule_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling PATCH requests to /switcher/enable_schedule.

    Accepts raw schedule_data str in url or body.
    Returns a json object represnting the request status.
    """
    try:
        if request.args and consts.PARAM_SCHEDULE_DATA in request.args:
            schedule_data = request.args[consts.PARAM_SCHEDULE_DATA][0]
        elif request.json and consts.PARAM_SCHEDULE_DATA in request.json:
            schedule_data = str(request.json[consts.PARAM_SCHEDULE_DATA])
        else:
            raise InvalidUsage("Argument schedule_data is missing.", 400)
        if len(schedule_data) != 24:
            raise InvalidUsage(
                "Argument schedule_data is length is no 24.", 400
            )
        updated_schedule_data = (
            schedule_data[0:2] + ENABLE_SCHEDULE + schedule_data[4:]
        )

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.disable_enable_schedule(
                updated_schedule_data
            )

        if (
            response
            and response.msg_type
            == messages.ResponseMessageType.DISABLE_ENABLE_SCHEDULE
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed enabling the schedule.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed enabling the schedule.", 500) from exc


async def disable_schedule_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling PATCH requests to /switcher/disable_schedule.

    Accepts raw schedule_data str in url or body.
    Returns a json object represnting the request status.
    """
    try:
        if request.args and consts.PARAM_SCHEDULE_DATA in request.args:
            schedule_data = request.args[consts.PARAM_SCHEDULE_DATA][0]
        elif request.json and consts.PARAM_SCHEDULE_DATA in request.json:
            schedule_data = str(request.json[consts.PARAM_SCHEDULE_DATA])
        else:
            raise InvalidUsage("Argument schedule_data is missing.", 400)
        if len(schedule_data) != 24:
            raise InvalidUsage(
                "Argument schedule_data is length is no 24.", 400
            )
        updated_schedule_data = (
            schedule_data[0:2] + DISABLE_SCHEDULE + schedule_data[4:]
        )

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.disable_enable_schedule(
                updated_schedule_data
            )

        if (
            response
            and response.msg_type
            == messages.ResponseMessageType.DISABLE_ENABLE_SCHEDULE
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed disabling the schedule.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed disabling the schedule.", 500) from exc


async def delete_schedule_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling DELETE requests to /switcher/delete_schedule.

    Accepts schedule_id integer (0-7) represnting the schedule in url or body.
    Returns a json object represnting the request status.
    """
    try:
        if request.args and consts.PARAM_SCHEDULE_ID in request.args:
            schedule_id = str(request.args[consts.PARAM_SCHEDULE_ID][0])
        elif request.json and consts.PARAM_SCHEDULE_ID in request.json:
            schedule_id = str(request.json[consts.PARAM_SCHEDULE_ID])
        else:
            raise InvalidUsage("Argument schedule_id is missing.", 400)
        if int(schedule_id) < 0 or int(schedule_id) > 7:
            raise InvalidUsage("Argument schedule_id accepts values 0-7.", 400)

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.delete_schedule(schedule_id)

        if (
            response
            and response.msg_type
            == messages.ResponseMessageType.DELETE_SCHEDULE
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed deleting the schedule.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed deleting the schedule.", 500) from exc


def _validate_day_to_int(day: str) -> int:
    """Use for validating weekdays input from create schedule request."""
    if day not in WEEKDAY_TUP:
        raise InvalidUsage(
            "Unrecognized day requests, check documentation.", 400
        )
    return DAY_TO_INT_DICT[day]


async def _create_raw_schedule_data(
    schedule_days: List[int],
    start_hours: int,
    start_minutes: int,
    stop_hours: int,
    stop_minutes: int,
) -> str:
    """Use for creating raw schedule data for creating schedule request."""
    running_loop = get_running_loop()

    weekdays = await create_weekdays_value(running_loop, schedule_days)
    start_time = await timedelta_str_to_schedule_time(
        running_loop, str(timedelta(hours=start_hours, minutes=start_minutes))
    )
    end_time = await timedelta_str_to_schedule_time(
        running_loop, str(timedelta(hours=stop_hours, minutes=stop_minutes))
    )
    return SCHEDULE_CREATE_DATA_FORMAT.format(weekdays, start_time, end_time)


def _validate_time_integers(
    start_hours: int, start_minutes: int, stop_hours: int, stop_minutes: int
) -> None:
    """Use to validate start and end time values for creating schedule."""
    if start_hours < 0 or start_hours > 23:
        raise InvalidUsage("Unknown start_hours, accepts 0 to 23.", 400)
    if start_minutes < 0 or start_minutes > 59:
        raise InvalidUsage("Unknown start_minutes, accepts 0 to 59.", 400)
    if stop_hours < 0 or stop_hours > 23:
        raise InvalidUsage("Unknown stop_hours, accepts 0 to 23.", 400)
    if stop_minutes < 0 or stop_minutes > 59:
        raise InvalidUsage("Unknown stop_minutes, accepts 0 to 59.", 400)


async def _parse_schedule_body(body: Dict) -> str:
    """Use for parsing the body of the create schedule request."""
    recurring = False
    days = []  # type: List[str]
    if consts.PARAM_DAYS in body:
        days = body[consts.PARAM_DAYS]
        recurring = True
    if consts.PARAM_START_HOURS in body:
        start_hours = int(body[consts.PARAM_START_HOURS])
    else:
        raise InvalidUsage("Argument start_hours is missing.", 400)
    if consts.PARAM_START_MINUTES in body:
        start_minutes = int(body[consts.PARAM_START_MINUTES])
    else:
        raise InvalidUsage("Argument start_minutes is missing.", 400)
    if consts.PARAM_STOP_HOURS in body:
        stop_hours = int(body[consts.PARAM_STOP_HOURS])
    else:
        raise InvalidUsage("Argument stop_hours is missing.", 400)
    if consts.PARAM_STOP_MINUTES in body:
        stop_minutes = int(body[consts.PARAM_STOP_MINUTES])
    else:
        raise InvalidUsage("Argument stop_minutes is missing.", 400)

    _validate_time_integers(
        start_hours, start_minutes, stop_hours, stop_minutes
    )

    schedule_days = [0]
    if recurring:
        for day in days:
            schedule_days.append(_validate_day_to_int(day))

    return await _create_raw_schedule_data(
        schedule_days, start_hours, start_minutes, stop_hours, stop_minutes
    )


async def create_schedule_handler(
    request: Request,
    ip_address: str,
    phone_id: str,
    device_id: str,
    device_password: str,
) -> HTTPResponse:
    """Use for handling PUT requests to /switcher/create_schedule.

    Accepts json body only, no query parameters allowed!
    Accepts str list days, values:
    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
    Accepts integers start_hours, start_minutes, stop_hours, stop_minutes
    Returns a json object represnting the request status.
    """
    try:
        if not request.json:
            raise InvalidUsage("Json body is missing.", 400)

        schedule_data = await _parse_schedule_body(request.json)

        async with SwitcherV2Api(
            get_running_loop(),
            ip_address,
            phone_id,
            device_id,
            device_password,
        ) as swapi:
            response = await swapi.create_schedule(schedule_data)

        if (
            response
            and response.msg_type
            == messages.ResponseMessageType.CREATE_SCHEDULE
        ):
            return json({consts.KEY_SUCCESSFUL: response.successful})
        return json(
            {
                consts.KEY_SUCCESSFUL: False,
                consts.KEY_MESSAGE: "Failed creating the schedule.",
            }
        )
    except ExceptionSet as exc:
        raise ServerError("Failed creating the schedule.", 500) from exc
