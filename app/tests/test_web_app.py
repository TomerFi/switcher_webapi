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

from unittest.mock import AsyncMock, Mock, patch

from aiohttp import web
from assertpy import assert_that
from pytest import fixture

from .. import webapp

fake_device_params = "?id=ab1c2d&ip=1.2.3.4"


@fixture
async def api_client(aiohttp_client):
    # create application
    app = web.Application(middlewares=[webapp.error_middleware])
    app.add_routes(webapp.routes)
    # return client from application
    return await aiohttp_client(app)


@patch.object(webapp, "_serialize_object", return_value={"fake": "return_dict"})
@patch("aioswitcher.api.SwitcherApi.get_state")
@patch("aioswitcher.api.SwitcherApi.disconnect")
@patch("aioswitcher.api.SwitcherApi.connect", return_value=AsyncMock())
async def test_get_successful_get_state_request(
    connect, disconnect, get_state, serialize_object, api_client
):
    # stub get_state to return mock state response
    state_resp = Mock()
    get_state.return_value = state_resp
    # send get request for get_state endpoint
    response = await api_client.get(webapp.ENDPOINT_GET_STATE + fake_device_params)
    # assert mocks called and expected response
    connect.assert_called_once()  # connect is always called
    get_state.assert_called_once_with()
    serialize_object.assert_called_once_with(state_resp)
    disconnect.assert_called_once()  # diconnect is always called
    assert_that(response.status).is_equal_to(200)
    assert_that(await response.json()).contains_entry({"fake": "return_dict"})


@patch.object(webapp, "_serialize_object", return_value={"fake": "return_dict"})
@patch("aioswitcher.api.SwitcherApi.get_state", side_effect=Exception("blabla"))
@patch("aioswitcher.api.SwitcherApi.disconnect")
@patch("aioswitcher.api.SwitcherApi.connect", return_value=AsyncMock())
async def test_get_erroneous_get_state_request(
    connect, disconnect, get_state, serialize_object, api_client
):
    # send get request for get_state endpoint
    response = await api_client.get(webapp.ENDPOINT_GET_STATE + fake_device_params)
    # assert mocks called and expected response
    connect.assert_called_once()  # connect is always called
    get_state.assert_called_once_with()
    serialize_object.assert_not_called()
    disconnect.assert_called_once()  # diconnect is always called
    assert_that(response.status).is_equal_to(500)
    assert_that(await response.json()).contains_entry({"error": "blabla"})
