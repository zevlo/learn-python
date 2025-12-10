def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact list is empty.")

def main():
    contacts = {}
    favorite_contacts = set()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Add to Favorites")
        print("5. Display Favorites")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            name = input("Enter name to remove: ")
            remove_contact(contacts, name)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            name = input("Enter name to add to favorites: ")
            if name in contacts:
                favorite_contacts.add(name)
                print(f"{name} added to favorites.")
            else:
                print(f"Contact {name} not found.")
        elif choice == "5":
            print("\nFavorite Contacts:")
            for name in favorite_contacts:
                print(name)
        elif choice == "6":
            print("Thank you for using Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
