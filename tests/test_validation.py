import pytest

from contact_book.exceptions import ValidationError
from contact_book.validation import (
    validate_email,
    validate_name,
    validate_phone,
)


def test_valid_name():
    validate_name("Nour")


def test_invalid_name():
    with pytest.raises(ValidationError):
        validate_name("N0ur123")


def test_valid_phone():
    validate_phone("70123456")


def test_invalid_phone():
    with pytest.raises(ValidationError):
        validate_phone("123")


def test_valid_email():
    validate_email("nour@gmail.com")


def test_invalid_email():
    with pytest.raises(ValidationError):
        validate_email("nourgmail.com")