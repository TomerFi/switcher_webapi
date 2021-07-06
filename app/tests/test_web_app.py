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
from assertpy import assert_that
from pytest import fixture, mark

from .. import webapp

fake_device_qparams = "?" + webapp.KEY_ID + "=ab1c2d&" + webapp.KEY_IP + "=1.2.3.4"
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
    get_state,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub get_state to return mock state response
    get_state.return_value = response_mock
    # send get request for get_state endpoint: /switcher/get_state?id=ab1c2d&ip=1.2.3.4
    response = await api_client.get(webapp.ENDPOINT_GET_STATE + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    get_state.assert_called_once_with()
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.get_state", side_effect=Exception("blabla"))
async def test_erroneous_get_state_get_request(
    get_state, response_serializer, api_connect, api_disconnect, api_client
):
    # send get request for get_state endpoint: /switcher/get_state?id=ab1c2d&ip=1.2.3.4
    response = await api_client.get(webapp.ENDPOINT_GET_STATE + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    get_state.assert_called_once_with()
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@mark.parametrize("query_params,expected_values", [
    ("", (Command.ON, 0)),
    # &minutes=15
    ("&" + webapp.KEY_MINUTES + "=15", (Command.ON, 15)),
])
@patch("aioswitcher.api.SwitcherApi.control_device")
async def test_successful_turn_on_post_request(
    control_device,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
    query_params,
    expected_values,
):
    # stub control_device to return mock state response
    control_device.return_value = response_mock
    # send post request for turn_on endpoint: /switcher/turn_on?id=ab1c2d&ip=1.2.3.4...
    response = await api_client.post(webapp.ENDPOINT_TURN_ON + fake_device_qparams + query_params)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    control_device.assert_called_once_with(expected_values[0], expected_values[1])
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.control_device", side_effect=Exception("blabla"))
async def test_erroneous_turn_on_post_request(
    control_device, response_serializer, api_connect, api_disconnect, api_client
):
    # send post request for turn_on endpoint: /switcher/turn_on?id=ab1c2d&ip=1.2.3.4
    response = await api_client.post(webapp.ENDPOINT_TURN_ON + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    control_device.assert_called_once_with(Command.ON, 0)
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.control_device")
async def test_successful_turn_off_post_request(
    control_device,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub control_device to return mock state response
    control_device.return_value = response_mock
    # send post request for turn_off endpoint: /switcher/turn_off?id=ab1c2d&ip=1.2.3.4
    response = await api_client.post(webapp.ENDPOINT_TURN_OFF + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    control_device.assert_called_once_with(Command.OFF)
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.control_device", side_effect=Exception("blabla"))
async def test_erroneous_turn_off_post_request(
    control_device, response_serializer, api_connect, api_disconnect, api_client
):
    # send post request for turn_off endpoint: /switcher/turn_off?id=ab1c2d&ip=1.2.3.4
    response = await api_client.post(webapp.ENDPOINT_TURN_OFF + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    control_device.assert_called_once_with(Command.OFF)
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.set_device_name")
async def test_successful_set_name_patch_request(
    set_device_name,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
):
    # stub set_device_name to return mock state response
    set_device_name.return_value = response_mock
    # send patch request for set_name endpoint: /switcher/set_name?id=ab1c2d&ip=1.2.3.4&name=newFakedName
    response = await api_client.patch(webapp.ENDPOINT_SET_NAME + fake_device_qparams + "&" + webapp.KEY_NAME + "=newFakedName")
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    set_device_name.assert_called_once_with("newFakedName")
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.set_device_name", side_effect=Exception("blabla"))
async def test_erroneous_set_name_patch_request(
    set_device_name, response_serializer, api_connect, api_disconnect, api_client
):
    # send patch request for set_name endpoint: /switcher/set_name?id=ab1c2d&ip=1.2.3.4&name=newFakedName
    response = await api_client.patch(webapp.ENDPOINT_SET_NAME + fake_device_qparams + "&" + webapp.KEY_NAME + "=newFakedName")
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    set_device_name.assert_called_once_with("newFakedName")
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})


@patch("aioswitcher.api.SwitcherApi.set_device_name")
async def test_set_name_faulty_no_name_patch_request(
    set_device_name, response_serializer, api_connect, api_disconnect, api_client
):
    # send patch request for set_name endpoint: /switcher/set_name?id=ab1c2d&ip=1.2.3.4
    response = await api_client.patch(webapp.ENDPOINT_SET_NAME + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_not_called()
    set_device_name.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "'name'"})


@mark.parametrize("query_params,expected_timedelta", [
    # &hours=2
    ("&" + webapp.KEY_HOURS + "=2", timedelta(hours=2)),
    # &hours=2&minutes=30
    ("&" + webapp.KEY_HOURS + "=2&" + webapp.KEY_MINUTES + "=30", timedelta(hours=2, minutes=30)),
])
@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown")
async def test_successful_set_auto_shutdown_patch_request(
    set_auto_shutdown,
    response_serializer,
    response_mock,
    api_connect,
    api_disconnect,
    api_client,
    query_params,
    expected_timedelta,
):
    # stub set_auto_shutdown to return mock state response
    set_auto_shutdown.return_value = response_mock
    # send patch request for set_auto_shutdown endpoint: /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4...
    response = await api_client.patch(webapp.ENDPOINT_SET_AUTO_SHUTDOWN + fake_device_qparams + query_params)
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    set_auto_shutdown.assert_called_once_with(expected_timedelta)
    response_serializer.assert_called_once_with(response_mock)
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry(fake_serialized_data)


@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown")
async def test_set_auto_shutdown_with_faulty_no_hours_patch_request(
    set_auto_shutdown, response_serializer, api_connect, api_disconnect, api_client
):
    # send patch request for set_auto_shutdown endpoint: /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4&hours=2
    response = await api_client.patch(webapp.ENDPOINT_SET_AUTO_SHUTDOWN + fake_device_qparams)
    # verify mocks calling
    api_connect.assert_not_called()
    set_auto_shutdown.assert_not_called()
    response_serializer.assert_not_called()
    api_disconnect.assert_not_called()
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "'hours'"})


@patch("aioswitcher.api.SwitcherApi.set_auto_shutdown", side_effect=Exception("blabla"))
async def test_erroneous_set_auto_shutdown_patch_request(
    set_auto_shutdown, response_serializer, api_connect, api_disconnect, api_client
):
    # send patch request for set_auto_shutdown endpoint: /switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4&hours=2
    response = await api_client.patch(webapp.ENDPOINT_SET_AUTO_SHUTDOWN + fake_device_qparams + "&" + webapp.KEY_HOURS + "=2")
    # verify mocks calling
    api_connect.assert_called_once()  # connect is always called
    set_auto_shutdown.assert_called_once_with(timedelta(hours=2))
    response_serializer.assert_not_called()
    api_disconnect.assert_called_once()  # diconnect is always called
    # assert the expected response
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})
