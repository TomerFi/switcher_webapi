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

"""Test cases for access logger custom implementation."""

from unittest.mock import Mock, patch

from pytest import fixture

from ..webapp import CustomAccessLogger


@fixture
def mock_request():
    request = Mock()
    request.remote = "127.0.0.1"
    request.method = "GET"
    request.path = "/switcher/get_state"
    return request


@fixture
def mock_response():
    response = Mock()
    response.status = 200
    return response


@fixture
def mock_logger():
    return Mock()


def test_access_logger_implementation_writing_to_debug_level(
    mock_logger, mock_request, mock_response
):
    with patch.object(mock_logger, "debug") as mock_debug:
        sut_impl = CustomAccessLogger(mock_logger, "")
        sut_impl.log(mock_request, mock_response, 0.314159)

        mock_debug.assert_called_once_with(
            "127.0.0.1 GET /switcher/get_state done in 0.314159s: 200"
        )
