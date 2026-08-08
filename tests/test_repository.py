from contact_book.models import Contact
from contact_book.repository import (
    add_contact,
    delete_contact,
    find_contact,
    list_contacts,
    update_contact,
)


#def test_add_contact():
def test_add_contact(sample_contact):
    contacts = []
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Family",
        "2026-08-06"
    )'''

    add_contact(contacts, sample_contact)
    assert len(contacts) == 1
    assert contacts[0].name == sample_contact.name

#def test_find_contact():
def test_find_contact(sample_contact):
    contacts = []
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''
    add_contact(contacts, sample_contact)
    result = find_contact(contacts, 1)
    assert result == sample_contact

#def test_delete_contact():
def test_delete_contact(sample_contact):
    contacts = []
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''
    add_contact(contacts, sample_contact)
    delete_contact(contacts, 1)
    assert len(contacts) == 0


#def test_update_contact():
def test_update_contact(sample_contact):
    contacts = []
    '''old_contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''

    add_contact(contacts, sample_contact)
    new_contact = Contact(
        1,
        "Aya",
        "03123456",
        "aya@gmail.com",
        "Work",
        "2026-08-07"
    )

    update_contact(contacts, 1, new_contact)
    assert contacts[0].name == "Aya"
    assert contacts[0].phone == "03123456"
    assert contacts[0].email == "aya@gmail.com"
    assert contacts[0].group == "Work"


#def test_list_contacts():
def test_list_contacts(sample_contact):
    contacts = []
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''
    add_contact(contacts, sample_contact)
    result = list_contacts(contacts)
    assert len(result) == 1
    assert result[0].name == sample_contact.name