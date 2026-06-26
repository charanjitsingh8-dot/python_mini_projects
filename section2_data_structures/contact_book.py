contacts = {}
used_numbers = set()

def add_contact():
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()

    if number in used_numbers:
        print("This number already exists in another contact.")
        return

    contacts[name] = number
    used_numbers.add(number)
    print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}  |  Number: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    new_number = input("Enter new phone number: ").strip()

    if new_number in used_numbers:
        print("This number already exists in another contact.")
        return

    used_numbers.discard(contacts[name])
    contacts[name] = new_number
    used_numbers.add(new_number)
    print(f"Contact '{name}' updated successfully.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    used_numbers.discard(contacts[name])
    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")

def show_all_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n" + "=" * 35)
    print("         ALL CONTACTS")
    print("=" * 35)
    for name, number in contacts.items():
        print(f"  {name}  :  {number}")
    print("=" * 35)

def main():
    print("=" * 35)
    print("        Contact Book")
    print("=" * 35)

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")
        print("-" * 35)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()