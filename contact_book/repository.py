from .models import Contact


def add_contact(contacts: list, contact: Contact) -> None:
    contacts.append(contact)

def find_contact(contacts: list, contact_id: int) -> Contact | None:
    for contact in contacts:
        if contact.id == contact_id:
            return contact
    return None

def delete_contact(contacts: list, contact_id: int) -> bool:
    contact = find_contact(contacts, contact_id)

    if contact is not None:
        contacts.remove(contact)
        return True
    return False

def update_contact(contacts: list, contact_id: int, new_contact: Contact) -> bool:
    contact = find_contact(contacts, contact_id)

    if contact is not None:
        if new_contact.name != "":
            contact.name = new_contact.name
        if new_contact.phone != "":
            contact.phone = new_contact.phone
        if new_contact.email != "":
                    contact.email = new_contact.email
        if new_contact.group != "":
                    contact.group = new_contact.group
        if new_contact.added != "":
                    contact.added = new_contact.added
        return True
    return False

def list_contacts(contacts: list) -> list:
    return sorted(contacts, key=lambda c: (
        c.name.split()[-1].lower(),
        c.name.split()[0].lower()
    ))

def search_contacts(contacts: list, query: str) -> list:
    results = []
    query = query.lower()
    for contact in contacts:
        if (
            query in contact.name.lower()
            or query in contact.email.lower()
            or query in contact.phone
        ):
            results.append(contact)
    return results