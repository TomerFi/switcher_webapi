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
