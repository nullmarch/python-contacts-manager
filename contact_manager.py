# Simple contact book
# A command-line application to add, search and view contacts.

contacts = []  # List to store contact dictionaries
active = True  # Controls the main application loop

# Add contact function
def add_contact(contacts):
    duplicate_found = False  # Reset flag before each add attempt
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    # Validate input — reject empty fields
    if name.strip() == '' or phone.strip() == '':
        print("Name and phone cannot be empty.")
        return
    # Check for duplicates before adding
    for contact in contacts:
        if name in contact['name'] or phone in contact['phone']:
            duplicate_found = True

    # Only add if no duplicate was found
    if not duplicate_found :
        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        print("Contact added successfully!")
    else:
        print("Name or phone already exists.")

# Modify contact function
def modify_contact(contacts):
    search = input("Enter contact name or phone number: ")
    contact_found = False
    contact_result = None 

    if search != '':
        if contacts:
            for contact in contacts:
                if search.lower().strip() in contact["name"] or search.lower().strip() in contact["phone"]:
                    contact_found = True
                    contact_result = contact

            if contact_found:
                print(f"Contact found: \nName: {contact_result['name'].title()} | Phone: {contact_result['phone']}")
                new_name = input("Enter new contact name: ")
                new_phone = input("Enter new phone number: ")

                if new_name != '':
                    contact_result['name'] = new_name

                if new_phone != '':
                    contact_result["phone"] = new_phone

                print("Changes Applied")
            else:
                print("contact not found.")
        else:
                print("Contact list is empty.")        
    else:
        print("Please enter a value!")

# View contact function
def view_contact(contacts):
    if contacts:    # Only display if list not empty
        counter = 0
        print("\nContacts:")
        for contact in contacts:
            counter += 1
            print(f"{counter}- Name: {contact['name'].title()} | Phone: {contact['phone']}.")
    else:
        print("The contacts list is empty!")

# Search contact function
def search_contact(contacts):
    search = input("Enter contact name or phone number: ")
    contact_found = False
    contact_result = None

    if search != '':
        if contacts:    # Only search if list is not empty
            for contact in contacts:
                if search.lower().strip() in contact["name"] or search.lower().strip() in contact["phone"]:
                    contact_found = True
                    contact_result = contact

            # Decision made outside loop after full scan
            if contact_found:        
                print(f"Contact found: \nName: {contact_result['name'].title()} | Phone: {contact_result['phone']}")
            else:
                print("contact not found.")
        else:
            print("Contact list is empty.")
    else: 
        print("Please enter a value!")

# Delete contact function
def delete_contact(contacts):
    search = input("Enter contact name or phone number: ")
    contact_found = False
    contact_result = None

    if search != '':
        
        if contacts: 
            for contact in contacts:
                if search.lower() in contact["name"].lower() or search in contact["phone"]:
                    contact_found = True
                    contact_result = contact
        else:
            print("Contact list is empty.")

        if contact_found:
            confirm = input(f"Delete {contact_result['name'].title()} | {contact_result['phone']}? (Yes/No): ")
            if confirm.lower().strip() == 'yes':
                contacts.remove(contact_result)
                print("Contact removed!")
            else:
                print("Deletion cancelled.")
        else: 
            print("Contact not found!")
    else:
        print("Please enter a value!")

while active:
    task = input("Do you want to add, modify, search or view contacts? (add/search/view/modify/delete/exit) " )
   
    # --- ADD CONTACTS ---.
    if task.lower().strip() == 'add':
        add_contact(contacts)
    
    # --- MODIFY CONTACTS ---.
    elif task.lower().strip() == "modify":
        modify_contact(contacts)


    # --- VIEW CONTACTS ---
    elif task.lower().strip() == 'view':
        view_contact(contacts)
        
    # --- SEARCH CONTACTS ---
    elif task.lower().strip() == 'search':
        search_contact(contacts)
        
    # --- DELETE ---
    elif task.lower().strip() == 'delete':
        delete_contact(contacts)

    # --- EXIT ---
    elif task.lower().strip() == 'exit':
        print("Goodbye!")
        active = False
        break

    # --- INVALID INPUT ---
    else:
        print("Invalid option, please type add, search, view, or exit.")

    


