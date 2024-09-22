import json
import os
CONTACTS_FILE = "contacts.json"
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    search_term = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower():
            print(f"\nCurrent details of {contact['name']}:")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(contacts):
    search_term = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if search_term in contact['name'].lower():
            print(f"Deleting contact: {contact['name']}")
            del contacts[i]
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting the contact management system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
