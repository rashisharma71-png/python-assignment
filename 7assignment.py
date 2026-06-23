import csv
while True:
    print("\n----- ADDRESS BOOK -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")

        contact = [name, mobile, email]

        file = open("address_book.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow(contact)
        file.close()

        print("Contact Added Successfully!")

    elif choice == "2":
        file = open("address_book.csv", "r")
        reader = csv.reader(file)

        print("\nContacts List:")
        for row in reader:
            print(row)

        file.close()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")