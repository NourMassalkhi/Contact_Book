import json
from pathlib import Path

from .models import Contact

file=Path ("data/contacts.json")
def load_contacts():
    try:
        with open(file, "r") as f:
            data = json.load(f)
        contacts = []
        for data_content in data:
            contacts.append(Contact.from_dict(data_content))
        return contacts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File is corrupted/starting with empty contacts")
        return []
    
def save_contacts(contacts):
    data=[]
    for contact  in contacts:
        data.append (contact.to_dict())
    with open (file, "w") as f:
        json.dump (data, f, indent=4)

    