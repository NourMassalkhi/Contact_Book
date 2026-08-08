from contact_book import storage
from contact_book.storage import load_contacts, save_contacts


#def test_save_and_load_contacts(tmp_path):
def test_save_and_load_contacts(tmp_path, sample_contact):
    storage.file = tmp_path / "contacts.json"
    contacts=[sample_contact]
    save_contacts(contacts)
    loaded_contacts = load_contacts()

    assert len(loaded_contacts) == 1
    assert loaded_contacts[0].id == sample_contact.id
    assert loaded_contacts[0].name == sample_contact.name
    assert loaded_contacts[0].phone == sample_contact.phone
    assert loaded_contacts[0].email == sample_contact.email
    assert loaded_contacts[0].group == sample_contact.group
    assert loaded_contacts[0].added == sample_contact.added