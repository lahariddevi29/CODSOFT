contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully!")

def view_contact_list():
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(query):
    search_results = []
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone']:
            search_results.append((name, info))
    return search_results

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Current Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        option = input("What do you want to update? (phone/email/address): ").lower()
        if option == 'phone':
            contacts[name]['phone'] = input("Enter new phone number: ")
        elif option == 'email':
            contacts[name]['email'] = input("Enter new email: ")
        elif option == 'address':
            contacts[name]['address'] = input("Enter new address: ")
        else:
            print("Invalid option.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    print("Welcome to Contact Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_results = search_contact(query)
            if search_results:
                print("\nSearch Results:")
                for name, info in search_results:
                    print(f"Name: {name}, Phone: {info['phone']}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
