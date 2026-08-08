import pytest

from contact_book.models import Contact


@pytest.fixture
def sample_contact():
    return Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )