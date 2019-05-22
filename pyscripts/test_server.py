"""Unit tests for the Switcher WebAPI."""

from aiohttp import ClientSession
from aioswitcher.api.messages import ResponseMessageType
from aioswitcher.consts import STATE_ON, WEEKDAY_TUP
from asynctest import MagicMock, patch
from bs4 import BeautifulSoup

import consts
from helpers import get_local_ip_address, get_next_weekday
import mappings


BASE_URL_FORMAT = (
    'http://' + get_local_ip_address()
    + ':' + str(consts.TEST_SERVER_PORT) + '{}')

URL_GET_STATE = BASE_URL_FORMAT.format(mappings.URL_MAPPING_GET_STATE)
URL_TURN_ON = BASE_URL_FORMAT.format(mappings.URL_MAPPING_TURN_ON)
URL_TURN_OFF = BASE_URL_FORMAT.format(mappings.URL_MAPPING_TURN_OFF)
URL_GET_SCHEDULES = BASE_URL_FORMAT.format(mappings.URL_MAPPING_GET_SCHEDULES)
URL_SET_AUTO_SHUTDOWN = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_SET_AUTO_SHUTDOWN)
URL_SET_DEVICE_NAME = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_SET_DEVICE_NAME)
URL_ENABLE_SCHEDULE = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_ENABLE_SCHEDULE)
URL_DISABLE_SCHEDULE = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_DISABLE_SCHEDULE)
URL_DELETE_SCHEDULE = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_DELETE_SCHEDULE)
URL_CREATE_SCHEDULE = \
    BASE_URL_FORMAT.format(mappings.URL_MAPPING_CREATE_SCHEDULE)


async def test_get_state_request(get_state_response: MagicMock) -> None:
    """Test /switcher/get_state request."""
    with patch('request_handlers.SwitcherV2Api.get_state',
               return_value=get_state_response) as patcher:
        async with ClientSession() as session:
            async with session.get(URL_GET_STATE) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]
                assert body[consts.KEY_STATE] == STATE_ON
                assert body[consts.KEY_TIME_LEFT] == consts.DUMMY_TIME_LEFT
                assert body[consts.KEY_AUTO_OFF] == consts.DUMMY_AUTO_OFF
                assert body[consts.KEY_POWER_CONSUMPTION] == \
                    consts.DUMMY_POWER_CONSUMPTION
                assert body[consts.KEY_ELECTRIC_CURRENT] == \
                    consts.DUMMY_ELECTRIC_CURRENT

        get_state_response.init_future.result().successful = False
        async with ClientSession() as session:
            async with session.get(URL_GET_STATE) as response:
                assert response.status == 200

                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]

            patcher.return_value = None
            async with session.get(URL_GET_STATE) as response:
                assert response.status == 503

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Failed to get response from api."


async def test_turn_off_request(control_response: MagicMock) -> None:
    """Test /switcher/turn_off request."""
    with patch('request_handlers.SwitcherV2Api.control_device',
               return_value=control_response):
        async with ClientSession() as session:
            async with session.post(URL_TURN_OFF) as response:
                assert response.status == 200
                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            control_response.successful = False
            async with session.post(URL_TURN_OFF) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE not in body

            control_response.msg_type = ResponseMessageType.STATE
            async with session.post(URL_TURN_OFF) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


async def test_turn_on_request(control_response: MagicMock) -> None:
    """Test /switcher/turn_on request."""
    with patch('request_handlers.SwitcherV2Api.control_device',
               return_value=control_response):
        async with ClientSession() as session:
            async with session.post(URL_TURN_ON) as response:
                assert response.status == 200
                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_TURN_ON,
                    params={consts.PARAM_MINUTES: 30}) as response:
                assert response.status == 200
                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_TURN_ON,
                    **{'json': {consts.PARAM_MINUTES: 30}}) as response:
                assert response.status == 200
                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_TURN_ON,
                    params={consts.PARAM_MINUTES: 181}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Can only accept timer for 1 to 180 minutes."

            control_response.msg_type = ResponseMessageType.STATE
            async with session.post(URL_TURN_ON) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body

            control_response.successful = False
            control_response.msg_type = ResponseMessageType.CONTROL
            async with session.post(URL_TURN_ON) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_TURN_ON,
                    params={consts.PARAM_MINUTES: 'noint'}) as response:
                assert response.status == 500
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.h1.text == "Internal Server Error"

            async with session.post(
                    URL_TURN_ON,
                    **{'json': {consts.PARAM_MINUTES: 'noint'}}) as response:
                assert response.status == 500
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.h1.text == "Internal Server Error"


async def test_get_schedules_request(
        get_schedules_response: MagicMock) -> None:
    """Test /switcher/get_schedules request."""
    with patch('request_handlers.SwitcherV2Api.get_schedules',
               return_value=get_schedules_response):
        async with ClientSession() as session:
            async with session.get(URL_GET_SCHEDULES) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]
                assert body[consts.KEY_FOUND_SCHEDULES]
                assert len(body[consts.KEY_SCHEDULES]) == 1
                assert body[consts.KEY_SCHEDULES][0][
                    consts.KEY_SCHEDULE_ID] == consts.DUMMY_SCHEDULE_ID
                assert body[consts.KEY_SCHEDULES][0][consts.KEY_ENABLED]
                assert body[consts.KEY_SCHEDULES][0][consts.KEY_RECURRING]

                assert len(body[consts.KEY_SCHEDULES][0][consts.KEY_DAYS]) == 1
                assert body[consts.KEY_SCHEDULES][0][consts.KEY_DAYS][0] == \
                    WEEKDAY_TUP[get_next_weekday()]

                assert body[consts.KEY_SCHEDULES][0][
                    consts.KEY_START_TIME] == consts.DUMMY_START_TIME
                assert body[consts.KEY_SCHEDULES][0][
                    consts.KEY_END_TIME] == consts.DUMMY_END_TIME
                assert body[consts.KEY_SCHEDULES][0][
                    consts.KEY_DURATION] == consts.DUMMY_DURATION

            get_schedules_response.successful = False
            async with session.get(URL_GET_SCHEDULES) as response:
                assert response.status == 200

                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]


async def test_set_auto_shutdown_request(
        set_auto_shutdown_response: MagicMock) -> None:
    """Test /switcher/set_auto_shutdown request."""
    with patch('request_handlers.SwitcherV2Api.set_auto_shutdown',
               return_value=set_auto_shutdown_response):
        async with ClientSession() as session:
            async with session.post(
                    URL_SET_AUTO_SHUTDOWN,
                    params={consts.PARAM_HOURS: '1',
                            consts.PARAM_MINUTES: '30'}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_SET_AUTO_SHUTDOWN,
                    **{'json': {consts.PARAM_HOURS: '1',
                                consts.PARAM_MINUTES: '30'}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_SET_AUTO_SHUTDOWN,
                    params={consts.PARAM_HOURS: '3',
                            consts.PARAM_MINUTES: '1'}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Auto shutdown can be set between 1 and 3 hours."

            async with session.post(URL_SET_AUTO_SHUTDOWN) as response:
                assert response.status == 400

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: One of the arguments hours or minutes is missing."

            set_auto_shutdown_response.msg_type = ResponseMessageType.STATE
            async with session.post(
                    URL_SET_AUTO_SHUTDOWN,
                    params={consts.PARAM_HOURS: '1',
                            consts.PARAM_MINUTES: '30'}) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


async def test_set_device_name_request(
        set_device_name_response: MagicMock) -> None:
    """Test /switcher/set_device_name request."""
    with patch('request_handlers.SwitcherV2Api.set_device_name',
               return_value=set_device_name_response):
        async with ClientSession() as session:
            async with session.post(
                    URL_SET_DEVICE_NAME,
                    params={consts.PARAM_NAME:
                            "new device name"}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_SET_DEVICE_NAME,
                    **{'json': {consts.PARAM_NAME:
                                "new device name"}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.post(
                    URL_SET_DEVICE_NAME,
                    params={consts.PARAM_NAME: 'x'}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Only accepts name with length between 2 and 32."

            async with session.post(URL_SET_DEVICE_NAME) as response:
                assert response.status == 400

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument name is missing."

            set_device_name_response.msg_type = ResponseMessageType.STATE
            async with session.post(
                    URL_SET_DEVICE_NAME,
                    params={consts.PARAM_NAME:
                            "new device name"}) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


async def test_enable_schedule_request(
        disable_enable_schedule_response: MagicMock) -> None:
    """Test /switcher/enable_schedule request."""
    with patch('request_handlers.SwitcherV2Api.disable_enable_schedule',
               return_value=disable_enable_schedule_response):
        async with ClientSession() as session:
            async with session.patch(
                    URL_ENABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            consts.DUMMY_SCHEDULE_DATA}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.patch(
                    URL_ENABLE_SCHEDULE,
                    **{'json': {consts.PARAM_SCHEDULE_DATA:
                                consts.DUMMY_SCHEDULE_DATA}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.patch(
                    URL_ENABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            'not_24_len'}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_data is length is no 24."

            async with session.patch(URL_ENABLE_SCHEDULE) as response:
                assert response.status == 400

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_data is missing."

            disable_enable_schedule_response.msg_type = \
                ResponseMessageType.STATE
            async with session.patch(
                    URL_ENABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            consts.DUMMY_SCHEDULE_DATA}) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


async def test_disable_schedule_request(
        disable_enable_schedule_response: MagicMock) -> None:
    """Test /switcher/disable_schedule request."""
    with patch('request_handlers.SwitcherV2Api.disable_enable_schedule',
               return_value=disable_enable_schedule_response):
        async with ClientSession() as session:
            async with session.patch(
                    URL_DISABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            consts.DUMMY_SCHEDULE_DATA}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.patch(
                    URL_DISABLE_SCHEDULE,
                    **{'json': {consts.PARAM_SCHEDULE_DATA:
                                consts.DUMMY_SCHEDULE_DATA}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.patch(
                    URL_DISABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            'not_24_len'}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_data is length is no 24."

            async with session.patch(URL_DISABLE_SCHEDULE) as response:
                assert response.status == 400

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_data is missing."

            disable_enable_schedule_response.msg_type = \
                ResponseMessageType.STATE
            async with session.patch(
                    URL_DISABLE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_DATA:
                            consts.DUMMY_SCHEDULE_DATA}) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


async def test_delete_schedule_request(
        delete_schedule_response: MagicMock) -> None:
    """Test /switcher/delete_schedule request."""
    with patch('request_handlers.SwitcherV2Api.delete_schedule',
               return_value=delete_schedule_response):
        async with ClientSession() as session:
            async with session.delete(
                    URL_DELETE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_ID: '2'}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.delete(
                    URL_DELETE_SCHEDULE,
                    **{'json': {consts.PARAM_SCHEDULE_ID: '2'}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.delete(
                    URL_DELETE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_ID: '8'}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_id accepts values 0-7."

            async with session.delete(URL_DELETE_SCHEDULE) as response:
                assert response.status == 400

                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument schedule_id is missing."

            delete_schedule_response.msg_type = ResponseMessageType.STATE
            async with session.delete(
                    URL_DELETE_SCHEDULE,
                    params={consts.PARAM_SCHEDULE_ID: '2'}) as response:
                assert response.status == 200
                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body


# pylint: disable=too-many-statements
async def test_create_schedule_request(
        create_schedule_response: MagicMock) -> None:
    """Test /switcher/create_schedule request."""
    with patch('request_handlers.SwitcherV2Api.create_schedule',
               return_value=create_schedule_response):
        async with ClientSession() as session:
            selected_test_day = WEEKDAY_TUP[get_next_weekday()]
            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '20',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 200

                body = await response.json()
                assert body[consts.KEY_SUCCESSFUL]

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '24',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Unknown start_hours, accepts 0 to 23."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_START_MINUTES: '60',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Unknown start_minutes, accepts 0 to 59."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '24',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Unknown stop_hours, accepts 0 to 23."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '60'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Unknown stop_minutes, accepts 0 to 59."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument start_hours is missing."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument start_minutes is missing."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument stop_hours is missing."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '23',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Argument stop_minutes is missing."

            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: ['Fakeday'],
                                consts.PARAM_START_HOURS: '20',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Unrecognized day requests, check documentation."

            async with session.put(URL_CREATE_SCHEDULE) as response:
                assert response.status == 400
                body = await response.text()
                bs4scrap = BeautifulSoup(body, 'html.parser')
                assert bs4scrap.text == \
                    "Error: Json body is missing."

            create_schedule_response.msg_type = ResponseMessageType.STATE
            async with session.put(
                    URL_CREATE_SCHEDULE,
                    **{'json': {consts.PARAM_DAYS: [selected_test_day],
                                consts.PARAM_START_HOURS: '20',
                                consts.PARAM_START_MINUTES: '0',
                                consts.PARAM_STOP_HOURS: '20',
                                consts.PARAM_STOP_MINUTES: '30'}}) as response:
                assert response.status == 200

                body = await response.json()
                assert not body[consts.KEY_SUCCESSFUL]
                assert consts.KEY_MESSAGE in body
# pylint: enable=too-many-statements
