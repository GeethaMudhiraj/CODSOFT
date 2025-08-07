contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def search_contact():
    keyword = input("Search by name or phone: ").lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print(f"Found: {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave blank to keep current value.")
            name = input(f"New name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"New phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"New email ({contacts[index]['email']}): ") or contacts[index]['email']
            address = input(f"New address ({contacts[index]['address']}): ") or contacts[index]['address']
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except:
        print("Invalid input.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except:
        print("Invalid input.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
