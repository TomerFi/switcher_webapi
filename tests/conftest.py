"""Fixtures and mockings for unit testing the Switcher WebAPI.

.. codeauthor:: Tomer Figenblat <tomer.figenblat@gmail.com>

"""

# fmt: off
from asyncio import (AbstractEventLoop, Future, StreamReader, StreamWriter,
                     get_event_loop, new_event_loop, set_event_loop)
from typing import Any, Generator
from unittest.mock import MagicMock, Mock, patch

from aioswitcher.api import messages
from aioswitcher.consts import STATE_ON, WEEKDAY_TUP
from aioswitcher.schedules import SwitcherV2Schedule
from pytest import fixture
from sanic import Sanic

from switcher_webapi import consts
from switcher_webapi.helpers import get_local_ip_address, get_next_weekday
from switcher_webapi.start_server import (CONF_DEVICE_ID, CONF_DEVICE_IP_ADDR,
                                          CONF_DEVICE_PASSWORD, CONF_PHONE_ID,
                                          CONF_THROTTLE, sanic_app)

# fmt: on


@fixture(name="control_response")
def mock_control_response() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the control response.

    Yields:
      Mocked ``SwitcherV2ControlResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2ControlResponseMSG)
    mock_response.successful = True
    mock_response.msg_type = messages.ResponseMessageType.CONTROL

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2ControlResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="create_schedule_response")
def mock_create_schedule_request() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the create_schedule response.

    Yields:
      Mocked ``SwitcherV2CreateScheduleResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2CreateScheduleResponseMSG)
    mock_response.successful = True
    mock_response.msg_type = messages.ResponseMessageType.CREATE_SCHEDULE

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2CreateScheduleResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="delete_schedule_response")
def mock_delete_schedule_request() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the delete_schedule response.

    Yields:
      Mocked ``SwitcherV2DeleteScheduleResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2DeleteScheduleResponseMSG)
    mock_response.successful = True
    mock_response.msg_type = messages.ResponseMessageType.DELETE_SCHEDULE

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2DeleteScheduleResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="disable_enable_schedule_response")
def mock_disable_enable_schedule_request() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the disable_enable_schedule response.

    Yields:
      Mocked ``SwitcherV2DisableEnableScheduleResponseMSG`` object.

    """
    mock_response = MagicMock(
        messages.SwitcherV2DisableEnableScheduleResponseMSG
    )
    mock_response.successful = True
    mock_response.msg_type = (
        messages.ResponseMessageType.DISABLE_ENABLE_SCHEDULE
    )

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2DisableEnableScheduleResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="get_schedules_response")
def mock_get_schedules_response(
    schedule_object,
) -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the get_schedules response.

    Args:
      schedule_object: Fixture of mocked ``SwitcherV2Schedule`` object.

    Yields:
      Mocked ``SwitcherV2GetScheduleResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2GetScheduleResponseMSG)
    mock_response.successful = True
    mock_response.found_schedules = True
    mock_response.get_schedules = [schedule_object]
    mock_response.msg_type = messages.ResponseMessageType.GET_SCHEDULES

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2GetScheduleResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="get_state_response")
def mock_get_state_response() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the get_state response.

    Yields:
      Mocked ``SwitcherV2StateResponseMSG`` object.

    """
    mock_future_response = MagicMock(messages.SwitcherV2StateResponseMSG)
    mock_future_response.successful = True
    mock_future_response.state = STATE_ON
    mock_future_response.time_left = consts.DUMMY_TIME_LEFT
    mock_future_response.time_on = consts.DUMMY_TIME_ON
    mock_future_response.auto_off = consts.DUMMY_AUTO_OFF
    mock_future_response.power = consts.DUMMY_POWER_CONSUMPTION
    mock_future_response.current = consts.DUMMY_ELECTRIC_CURRENT
    mock_future_response.msg_type = messages.ResponseMessageType.STATE

    mock_initial_response = MagicMock(messages.SwitcherV2StateResponseMSG)
    mock_initial_response.init_future = Future()
    mock_initial_response.init_future.set_result(mock_future_response)

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2StateResponseMSG",
        new=mock_initial_response,
    ) as patcher:
        yield patcher


@fixture(name="loop", scope="session")
def mock_loop() -> Generator[AbstractEventLoop, Any, None]:
    """Fixture for running an event loop.

    Yields:
      Test event loop for running test server.

    """
    set_event_loop(new_event_loop())
    loop = get_event_loop()
    yield loop


@fixture(name="sanic_test_app", scope="session")
def mock_sanic_test_app() -> Generator[Sanic, Any, None]:
    """Fixture for creating a test instance on the sanic app.

    Yields:
      Test sanic application for mocking testing server.

    """
    test_app = sanic_app
    test_app.config[CONF_PHONE_ID] = "1234"
    test_app.config[CONF_DEVICE_ID] = "ab1c2d"
    test_app.config[CONF_DEVICE_PASSWORD] = "12345678"
    test_app.config[CONF_DEVICE_IP_ADDR] = "192.168.100.157"
    test_app.config[CONF_THROTTLE] = "0.1"

    yield test_app


@fixture(name="schedule_object")
def mock_schedule_object() -> Generator[None, None, SwitcherV2Schedule]:
    """Fixture for the aioswitcher.schedules.SwitcherV2Schedule object.

    Returns:
      Mocked ``SwitcherV2Schedule`` object.

    """
    mock_object = MagicMock(SwitcherV2Schedule)
    mock_object.schedule_id = consts.DUMMY_SCHEDULE_ID
    mock_object.enabled = True
    mock_object.recurring = True
    mock_object.days = [WEEKDAY_TUP[get_next_weekday()]]
    mock_object.start_time = consts.DUMMY_START_TIME
    mock_object.end_time = consts.DUMMY_END_TIME
    mock_object.duration = consts.DUMMY_DURATION

    mock_initial_response = MagicMock(SwitcherV2Schedule)
    mock_initial_response.init_future = Future()
    mock_initial_response.init_future.set_result(mock_object)

    return mock_initial_response


@fixture(name="set_auto_shutdown_response")
def mock_set_auto_shutdown_response() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the set_auto_shutdown response.

    Yields:
      Mocked ``SwitcherV2SetAutoOffResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2SetAutoOffResponseMSG)
    mock_response.successful = True
    mock_response.msg_type = messages.ResponseMessageType.AUTO_OFF

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2SetAutoOffResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="set_device_name_response")
def mock_set_device_name_response() -> Generator[MagicMock, Any, None]:
    """Fixture for mocking the set_device_name response.

    Yields:
      Mocked ``SwitcherV2UpdateNameResponseMSG`` object.

    """
    mock_response = MagicMock(messages.SwitcherV2UpdateNameResponseMSG)
    mock_response.successful = True
    mock_response.msg_type = messages.ResponseMessageType.UPDATE_NAME

    with patch(
        "switcher_webapi.request_handlers.messages.SwitcherV2UpdateNameResponseMSG",  # noqa:501
        new=mock_response,
    ) as patcher:
        yield patcher


@fixture(name="switcher_api_context_manager", scope="session", autouse=True)
def mock_switcher_api_context_manager() -> Generator[None, Any, None]:
    """Fixture for mocking the SwitcherV2Api context manager."""
    with patch("aioswitcher.api.SwitcherV2Api"):
        yield


@fixture(name="tcp_connection", scope="session", autouse=True)
def mock_tcp_connection() -> Generator[None, Any, None]:
    """Fixture for mocking asyncio.open_connection."""
    with patch(
        "aioswitcher.api.open_connection",
        return_value=(Mock(StreamReader), Mock(StreamWriter)),
    ):
        yield


@fixture(name="test_client", scope="session", autouse=True)
def mock_test_client(
    loop: AbstractEventLoop, sanic_test_app: Sanic
) -> Generator[None, None, AbstractEventLoop]:
    """Fixture for starting server in the event loop.

    Args:
      loop: Fixture of mocked ``AbstractEventLoop`` object.
      sanic_test_app: Fixture of mocked ``Sanic`` object.

    Returns:
      An event loop with a running server.

    """
    return loop.run_until_complete(
        sanic_test_app.create_server(
            host=get_local_ip_address(),
            port=consts.TEST_SERVER_PORT,
            return_asyncio_server=True,
        )
    )
