contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')
    
    if choice == '1':
        name = input('Enter your name: ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter age: ')
            email = input('Enter email: ')
            mobile = input('Enter mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact {name} has been created successfully!')
    
    elif choice == '2':
        name = input('Enter contact name to view: ')
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter contact name to update: ')
        if name in contacts:
            print(f'Updating contact for {name}')
            age = input('Enter new age: ')
            email = input('Enter new email: ')
            mobile = input('Enter new mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact {name} has been updated successfully!')
        else:
            print('Contact not found!')
    
    elif choice == '4':
        name = input('Enter contact name to delete: ')
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} has been deleted!')
        else:
            print('Contact not found!')
    
    elif choice == '5':
        name = input('Enter contact name to search: ')
        if name in contacts:
            print(f'Contact {name} exists in the contact book.')
        else:
            print('Contact not found!')

    elif choice == '6':
        print(f'Total number of contacts: {len(contacts)}')

    elif choice == '7':
        print('Exiting the Contact Book App.')
        break

    else:
        print('Invalid choice! Please enter a number between 1 and 7.')
