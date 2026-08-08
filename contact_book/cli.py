import csv

from .exceptions import ValidationError
from .models import Contact
from .repository import (
    add_contact,
    delete_contact,
    find_contact,
    list_contacts,
    update_contact,
)
from .storage import load_contacts, save_contacts
from .validation import (
    validate_email,
    validate_name,
    validate_phone,
)


def show_menu(contacts):
    print("\n")
    print("=" * 50)
    print("              CONTACT BOOK")
    print(f"              {len(contacts)} Contacts Loaded")
    print("=" * 50)
    print()
    print("[1] Add Contact")
    print("[2] List Contacts")
    print("[3] Find Contact")
    print("[4] Update Contact")
    print("[5] Delete Contact")
    print("[6] Export CSV")
    print("[7] Save & Exit")
    print("=" * 50)

def pause():
    input("\nPress Enter to return to menu")
def main():
    contacts = load_contacts()
    while True:
        show_menu(contacts)
        choice = input("Select an option")
        if choice == "1":
            print("\n" + "-" * 40)
            print("              Add Contact")
            print("-" * 40)

            try:
                id = input("ID            : ")
                name = input("Name        :")
                phone = input("Phone      : ")
                email = input("Email      : ")
                group = input("Group      : ")
                added = input("Added Date : ")
                validate_name(name)
                validate_phone(phone)
                validate_email(email)
                contact = Contact(
                    id,
                    name,
                    phone,
                    email,
                    group,
                    added,
                )
                exists = False
                for c in contacts:
                    if c.id == id or c.email == email or c.phone == phone:
                        exists = True
                        print("\n Contact already exists")
                        print("Existing contact:")
                        print(f"{c.id:<6}{c.name:<20}{c.phone:<15}{c.group}")
                        break
                if not exists:
                    add_contact(contacts, contact)
                    print(f'\n Contact "{name}" added successfully')
            except ValidationError as e:
                print("\nError:", e)
            pause()

        elif choice == "2":
            print("\n" + "-" * 100)
            all_contacts = list_contacts(contacts)

            if not all_contacts:
                print("No contacts found.")
            else:
               print(f"{'ID':<5} {'FIRST':<12} {'LAST':<12} {'PHONE':<15} {'EMAIL':<25} {'GROUP':<12} {'ADDED'}")
               print("-" * 100)
            for contact in all_contacts:
                    first_name = contact.name.split()[0]
                    last_name = contact.name.split()[-1]
                    print(
                        f"{contact.id:<5} "
                        f"{first_name:<12} "
                        f"{last_name:<12} "
                        f"{contact.phone:<15} "
                        f"{contact.email:<25} "
                        f"{contact.group:<12}"
                        f"{contact.added}"
                    )
            print("-" * 100)
            pause()

        elif choice == "3":
            print("\n" + "-" * 40)
            print("             Find Contact")
            print("-" * 40)
            print ("Search by:")
            print ("[1] Name")
            print ("[2] Phone:")
            print ("[3] Email:")
            option = input("Choose option: ")
            value = input("Enter search value: ")
            results = []

            for contact in contacts:
                if option == "1" and value.lower() in contact.name.lower() or option == "2" and value in contact.phone or option == "3" and value.lower() in contact.email.lower():
                 results.append(contact)
        
            if results:
                print("\n" + "-" * 100)
                print(f"{'ID':<5} {'NAME':<30} {'PHONE':<15} {'EMAIL':<25} {'GROUP':<12} {'ADDED'}")
                print("-" * 100)

                print(
                    f"{contact.id:<5}"
                    f"{contact.name:<30}"
                    f"{contact.phone:<15}"
                    f"{contact.email:<25}"
                    f"{contact.group:<12}"
                    f"{contact.added}")
                print("-" * 100)
            else:
                print("\nContact not found.")
            pause()

        elif choice == "4":
            print("\n" + "-" * 40)
            print("            Update Contact")
            print("-" * 40)
            contact_id = input("Enter Contact ID: ")
            contact = find_contact(contacts, contact_id)

            if contact:
                try:
                    name = input("New Name (leave blank to keep): ")
                    phone = input("New Phone (leave blank to keep): ")
                    email = input("New Email (leave blank to keep): ")
                    group = input("New Group (leave blank to keep): ")
                    added = input("New Added Date (leave blank to keep): ")

                    if name!="":
                        validate_name(name)
                    if phone!="":
                        validate_phone(phone)
                    if email!="":
                        validate_email(email)

                    new_contact = Contact(
                        contact_id,
                        name,
                        phone,
                        email,
                        group,
                        added,
                    )
                    update_contact(
                        contacts,
                        contact_id,
                        new_contact,
                    )
                    print("\nContact updated successfully!")
                except ValidationError as e:
                    print("\nError:", e)
            else:
                print("\nContact not found.")
            pause()

        elif choice == "5":
            print("\n" + "-" * 40)
            print("            Delete Contact")
            print("-" * 40)

            contact_id = input("Enter Contact ID; ")
            contact = find_contact(contacts, contact_id)
            if contact:
                confirm = input("Are you sure you want to delete? (y/n): ")
                if confirm.lower() == "y":
                    delete_contact(contacts, contact_id)
                    print(" Contact deleted successfullyy")
                else:
                    print("\nDeletion cancelled.")
            else:
                print("\nContact not found.")
            pause()

        elif choice == "7":
            save_contacts(contacts)
            print("\nContacts saved successfully.")
            print("Goodbye!\n")
            break

        elif choice == "6":
            with open ("contacts.csv", "w", newline="") as f:
                writer= csv.writer(f)
                writer.writerow(["ID", "Name", "Phone", "Email", "Group", "Added"])
                for contact in contacts:
                    writer.writerow([contact.id, contact.name, contact.phone, contact.email, contact.group, contact.added])
            print ("Contact exported successfully to contact.csv")
        else:
            print("\nInvalid option.")
            pause()