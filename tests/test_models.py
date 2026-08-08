from contact_book.models import Contact


#def test_create_contact():
def test_create_contact(sample_contact):
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''

    assert sample_contact.id == 1
    assert sample_contact.name == "Nour"
    assert sample_contact.phone == "70123456"
    assert sample_contact.email == "nour@gmail.com"
    assert sample_contact.group == "Friends"
    assert sample_contact.added == "2026-08-06"


#def test_to_dict():
def test_to_dict(sample_contact):
    '''contact = Contact(
        1,
        "Nour",
        "70123456",
        "nour@gmail.com",
        "Friends",
        "2026-08-06"
    )'''
    expected = {
        "id": 1,
        "name": "Nour",
        "phone": "70123456",
        "email": "nour@gmail.com",
        "group": "Friends",
        "added": "2026-08-06"
    }

    assert sample_contact.to_dict() == expected


#def test_from_dict():
def test_from_dict(sample_contact):
    data = {
        "id": 1,
        "name": "Nour",
        "phone": "70123456",
        "email": "nour@gmail.com",
        "group": "Friends",
        "added": "2026-08-06"
    }

    contact = Contact.from_dict(data)

    assert contact.id == sample_contact.id
    assert contact.name == sample_contact.name
    assert contact.phone == sample_contact.phone
    assert contact.email == sample_contact.email
    assert contact.group == sample_contact.group
    assert contact.added == sample_contact.added