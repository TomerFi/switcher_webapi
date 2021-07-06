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

"""Test cases for the web application."""

from datetime import timedelta
from unittest.mock import AsyncMock, Mock, patch

from aiohttp import web
from aioswitcher.api import Command
from aioswitcher.schedule import Days
from assertpy import assert_that
from pytest import fixture, mark

from .. import webapp

fake_device_qparams = f"{webapp.KEY_ID}=ab1c2d&{webapp.KEY_IP}=1.2.3.4"
fake_serialized_data = {"fake": "return_dict"}


@fixture
async def api_client(aiohttp_client):
    # create application
    app = web.Application(middlewares=[webapp.error_middleware])
    app.add_routes(webapp.routes)
    # return client from application
    return await aiohttp_client(app)


@fixture
def api_connect():
    with patch(
        "aioswitcher.api.SwitcherApi.connect", return_value=AsyncMock()
    ) as connect:
        yield connect


@fixture
def api_disconnect():
    with patch("aioswitcher.api.SwitcherApi.disconnect") as disconnect:
        yield disconnect


@fixture
def response_serializer():
    with patch.object(
        webapp, "_serialize_object", return_value=fake_serialized_data
    ) as serializer:
        yield serializer


@fixture
def response_mock():
    return Mock()


@patch("aioswitcher.api.SwitcherApi.get_state")
async def test_successful_get_state_get_request(
    api_get_state,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub api_get_state to return mock response
    api_get_state.return_value = response_mock
    # /switcher/get_state?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_GET_STATE}?{fake_device_qparams}"
    # send get request for get_state endpoint
    response = await api_client.get(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_get_state.assert_called_once_with()
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.get_state", side_effect=Exception("blabla"))
async def test_erroneous_get_state_get_request(
    api_get_state, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/get_state?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_GET_STATE}?{fake_device_qparams}"
    # send get request for get_state endpoint
    response = await api_client.get(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_get_state.assert_called_once_with()
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@mark.parametrize(
    "query_params,expected_values",
    [
        ("", (Command.ON, 0)),
        # &minutes=15
        ("&" + webapp.KEY_MINUTES + "=15", (Command.ON, 15)),
    ],
)
@patch("aioswitcher.api.SwitcherApi.control_device")
async def test_successful_turn_on_post_request(
    api_control_device,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
    query_params,
    expected_values,
):
    # stub api_control_device to return mock response
    api_control_device.return_value = response_mock
    # /switcher/turn_on?id=ab1c2d&ip=1.2.3.4...
    uri = f"{webapp.ENDPOINT_TURN_ON}?{fake_device_qparams}{query_params}"
    # send post request for turn_on endpoint
    response = await api_client.post(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_control_device.assert_called_once_with(expected_values[0], expected_values[1])
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.control_device", side_effect=Exception("blabla"))
async def test_erroneous_turn_on_post_request(
    api_control_device, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/turn_on?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_TURN_ON}?{fake_device_qparams}"
    # send post request for turn_on endpoint
    response = await api_client.post(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_control_device.assert_called_once_with(Command.ON, 0)
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.control_device")
async def test_successful_turn_off_post_request(
    api_control_device,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub api_control_device to return mock response
    api_control_device.return_value = response_mock
    # /switcher/turn_off?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_TURN_OFF}?{fake_device_qparams}"
    # send post request for turn_off endpoint
    response = await api_client.post(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_control_device.assert_called_once_with(Command.OFF)
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.control_device", side_effect=Exception("blabla"))
async def test_erroneous_turn_off_post_request(
    api_control_device, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/turn_off?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_TURN_OFF}?{fake_device_qparams}"
    # send post request for turn_off endpoint
    response = await api_client.post(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_control_device.assert_called_once_with(Command.OFF)
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.set_device_name")
async def test_successful_set_name_patch_request(
    api_set_device_name,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub api_set_device_name to return mock response
    api_set_device_name.return_value = response_mock
    # /switcher/set_name?id=ab1c2d&ip=1.2.3.4&name=newFakedName
    uri = f"{webapp.ENDPOINT_SET_NAME}?{fake_device_qparams}&{webapp.KEY_NAME}=newFakedName"
    # send patch request for set_name endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_set_device_name.assert_called_once_with("newFakedName")
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.set_device_name", side_effect=Exception("blabla"))
async def test_erroneous_set_name_patch_request(
    api_set_device_name, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/set_name?id=ab1c2d&ip=1.2.3.4&name=newFakedName
    uri = f"{webapp.ENDPOINT_SET_NAME}?{fake_device_qparams}&{webapp.KEY_NAME}=newFakedName"
    # send patch request for set_name endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_set_device_name.assert_called_once_with("newFakedName")
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.set_device_name")
async def test_set_name_faulty_no_name_patch_request(
    api_set_device_name, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/set_name?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_SET_NAME}?{fake_device_qparams}"
    # send patch request for set_name endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_not_called()
    api_set_device_name.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "'name'"})


@mark.parametrize(
    "query_params,expected_timedelta",
    [
        # $ hours=2
        (webapp.KEY_HOURS + "=2", timedelta(hours=2)),
        # & hours=2&minutes=30
        (
            webapp.KEY_HOURS + "=2&" + webapp.KEY_MINUTES + "=30",
            timedelta(hours=2, minutes=30),
        ),
    ],
)
@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown")
async def test_successful_set_auto_shutdown_patch_request(
    api_set_auto_shutdown,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
    query_params,
    expected_timedelta,
):
    # stub api_set_auto_shutdown to return mock response
    api_set_auto_shutdown.return_value = response_mock
    # /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4...
    uri = f"{webapp.ENDPOINT_SET_AUTO_SHUTDOWN}?{fake_device_qparams}&{query_params}"
    # send patch request for set_auto_shutdown endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_set_auto_shutdown.assert_called_once_with(expected_timedelta)
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown")
async def test_set_auto_shutdown_with_faulty_no_hours_patch_request(
    api_set_auto_shutdown, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_SET_AUTO_SHUTDOWN}?{fake_device_qparams}"
    # send patch request for set_auto_shutdown endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_not_called()
    api_set_auto_shutdown.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "'hours'"})


@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown", side_effect=Exception("blabla"))
async def test_erroneous_set_auto_shutdown_patch_request(
    api_set_auto_shutdown, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4&hours=2
    uri = f"{webapp.ENDPOINT_SET_AUTO_SHUTDOWN}?{fake_device_qparams}&{webapp.KEY_HOURS}=2"
    # send patch request for set_auto_shutdown endpoint
    response = await api_client.patch(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_set_auto_shutdown.assert_called_once_with(timedelta(hours=2))
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.get_schedules")
async def test_successful_get_schedules_get_request(
    api_get_schedules,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub mock response to return a set of two mock schedules
    schedule1 = schedule2 = Mock()
    response_mock.schedules = {schedule1, schedule2}
    # stub api_get_schedules to return mock response
    api_get_schedules.return_value = response_mock
    # /switcher/get_schedules?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_GET_SCHEDULES}?{fake_device_qparams}"
    # send get request for get_schedules endpoint
    response = await api_client.get(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_get_schedules.assert_called_once_with()
    response_serializer.assert_called_once_with(schedule1)
    response_serializer.assert_called_once_with(schedule2)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.get_schedules", side_effect=Exception("blabla"))
async def test_erroneous_get_schedules_get_request(
    api_get_schedules, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/get_schedules?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_GET_SCHEDULES}?{fake_device_qparams}"
    # send get request for get_schedules endpoint
    response = await api_client.get(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_get_schedules.assert_called_once_with()
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.delete_schedule")
async def test_successful_delete_schedule_delete_request(
    api_delete_schedule,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub api_delete_schedule to return mock response
    api_delete_schedule.return_value = response_mock
    # /switcher/delete_schedule?id=ab1c2d&ip=1.2.3.4&schedule=5
    uri = f"{webapp.ENDPOINT_DELETE_SCHEDULE}?{fake_device_qparams}&{webapp.KEY_SCHEDULE}=5"
    # send delete request for delete_schedule endpoint
    response = await api_client.delete(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_delete_schedule.assert_called_once_with("5")
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.delete_schedule")
async def test_delete_schedule_with_faulty_no_schedule_delete_request(
    api_delete_schedule, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/delete_schedule?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_DELETE_SCHEDULE}?{fake_device_qparams}"
    # send delete request for delete_schedule endpoint
    response = await api_client.delete(uri)
    # verify mocks calling
    api_connect.assert_not_called()
    api_delete_schedule.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "'schedule'"})


@patch("aioswitcher.api.SwitcherApi.delete_schedule", side_effect=Exception("blabla"))
async def test_errorneous_delete_schedule_delete_request(
    api_delete_schedule, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/delete_schedule?id=ab1c2d&ip=1.2.3.4&schedule=5
    uri = f"{webapp.ENDPOINT_DELETE_SCHEDULE}?{fake_device_qparams}&{webapp.KEY_SCHEDULE}=5"
    # send delete request for delete_schedule endpoint
    response = await api_client.delete(uri)
    # verify mocks calling
    api_connect.assert_called_once()
    api_delete_schedule.assert_called_once_with("5")
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@mark.parametrize(
    "json_body,expected_values",
    [
        (
            {webapp.KEY_START: "14:00", webapp.KEY_STOP: "15:30"},
            ("14:00", "15:30", set()),
        ),
        (
            {
                webapp.KEY_START: "13:30",
                webapp.KEY_STOP: "14:00",
                webapp.KEY_DAYS: ["Sunday", "Monday", "Friday"],
            },
            ("13:30", "14:00", {Days.SUNDAY, Days.MONDAY, Days.FRIDAY}),
        ),
        (
            {
                webapp.KEY_START: "18:15",
                webapp.KEY_STOP: "19:00",
                webapp.KEY_DAYS: [
                    "Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                ],
            },
            (
                "18:15",
                "19:00",
                {
                    Days.SUNDAY,
                    Days.MONDAY,
                    Days.TUESDAY,
                    Days.WEDNESDAY,
                    Days.THURSDAY,
                    Days.FRIDAY,
                    Days.SATURDAY,
                },
            ),
        ),
    ],
)
@patch("aioswitcher.api.SwitcherApi.create_schedule")
async def test_successful_create_schedule_post_request(
    api_create_schedule,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
    json_body,
    expected_values,
):
    # stub api_delete_schedule to return mock response
    api_create_schedule.return_value = response_mock
    # /switcher/create_schedule?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_CREATE_SCHEDULE}?{fake_device_qparams}"
    # send post request for create schedule endpoint
    response = await api_client.post(uri, json=json_body)
    # verify mocks calling
    api_connect.assert_called_once()
    api_create_schedule.assert_called_once_with(
        expected_values[0], expected_values[1], expected_values[2]
    )
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()
    # assert expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@mark.parametrize(
    "missing_key_json_body,expected_error_msg",
    [
        ({webapp.KEY_START: "18:15"}, "'stop'"),
        ({webapp.KEY_STOP: "19:00"}, "'start'"),
    ],
)
@patch("aioswitcher.api.SwitcherApi.create_schedule")
async def test_create_schedule_with_faulty_missing_key_post_request(
    api_create_schedule,
    response_serializer,
    api_connect,
    api_disconnect,
    api_client,
    missing_key_json_body,
    expected_error_msg,
):
    # /switcher/create_schedule?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_CREATE_SCHEDULE}?{fake_device_qparams}"
    # send post request for create schedule endpoint
    response = await api_client.post(uri, json=missing_key_json_body)
    # verify mocks calling
    api_connect.assert_not_called()
    api_create_schedule.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": expected_error_msg})


@patch("aioswitcher.api.SwitcherApi.create_schedule", side_effect=Exception("blabla"))
async def test_errorneous_create_schedule(
    api_create_schedule, response_serializer, api_connect, api_disconnect, api_client
):
    # /switcher/create_schedule?id=ab1c2d&ip=1.2.3.4
    uri = f"{webapp.ENDPOINT_CREATE_SCHEDULE}?{fake_device_qparams}"
    json_body = {webapp.KEY_START: "11:00", webapp.KEY_STOP: "11:15"}
    # send post request for create schedule endpoint
    response = await api_client.post(uri, json=json_body)
    # verify mocks calling
    api_connect.assert_called_once()
    api_create_schedule.assert_called_once_with("11:00", "11:15", set())
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})
