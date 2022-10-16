"""Test cases for the serialization helper function."""

from enum import Enum, auto
from unittest.mock import MagicMock

from assertpy import assert_that
from pytest import mark

from ..webapp import _serialize_object


class JustAnEnum(Enum):
    """Simple enum for testing serialization."""

    MEMBER_ONE = auto()
    MEMBER_TWO = auto()


@mark.parametrize(
    "sut_dict,expected_serialized_dict",
    [
        # just primitives, not modification of the dict is required
        (
            {
                "key_for_str": "stringstring",
                "key_for_int": 10,
                "key_for_set_str_to_list": {"anotherstring"},
            },
            {
                "key_for_str": "stringstring",
                "key_for_int": 10,
                "key_for_set_str_to_list": ["anotherstring"],
            },
        ),
        # key unparsed_response should be removed
        (
            {
                "key_for_str": "stringstring",
                "key_for_int": 10,
                "key_for_set_str_to_list": {"anotherstring"},
                "unparsed_response": b"010101",
            },
            {
                "key_for_str": "stringstring",
                "key_for_int": 10,
                "key_for_set_str_to_list": ["anotherstring"],
            },
        ),
        # enum members should be replaced with thier names
        (
            {
                "key_for_enum": JustAnEnum.MEMBER_ONE,
                "key_for_int": 10,
                "key_for_set_enum_to_list": {JustAnEnum.MEMBER_TWO},
                "unparsed_response": b"010101",
            },
            {
                "key_for_enum": "MEMBER_ONE",
                "key_for_int": 10,
                "key_for_set_enum_to_list": ["MEMBER_TWO"],
            },
        ),
    ],
)
def test_serialize_object(sut_dict, expected_serialized_dict):
    sut_obj = MagicMock()
    sut_obj.__dict__ = sut_dict

    assert_that(_serialize_object(sut_obj)).is_equal_to(expected_serialized_dict)
