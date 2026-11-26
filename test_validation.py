import pytest

from validation import validate_customer_id


def test_valid_customer_id():

    result = validate_customer_id(
        "5"
    )

    assert result == 5


def test_empty_customer_id():

    with pytest.raises(
        ValueError,
        match="Customer ID cannot be empty"
    ):

        validate_customer_id("")


def test_spaces_only_customer_id():

    with pytest.raises(
        ValueError,
        match="Customer ID cannot be empty"
    ):

        validate_customer_id("   ")


def test_text_customer_id():

    with pytest.raises(
        ValueError,
        match="Customer ID must be a number"
    ):

        validate_customer_id("abc")