books = ["Python", "Java", "C Programming", "Data Structures"]

while True:
    print("\nLibrary Management System")
    print("1. Display all books")
    print("2. Add a new book")
    print("3. Insert a book at a specific position")
    print("4. Check availability of a book")
    print("5. Count occurrences of a book")
    print("6. Remove a book")
    print("7. Sort books alphabetically")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nBooks in Library:")
        for i, book in enumerate(books, start=1):
            print(i, ".", book)

    elif choice == 2:
        book = input("Enter the new book title: ")
        books.append(book)
        print(book, "added successfully.")

    elif choice == 3:
        print("\nCurrent Books:")
        for i, book in enumerate(books, start=1):
            print(i, ".", book)

        position = int(input("Enter the position (0 to " + str(len(books)) + "): "))
        book = input("Enter the book title: ")

        if 0 <= position <= len(books):
            books.insert(position, book)
            print(book, "inserted successfully.")
        else:
            print("Invalid position.")

    elif choice == 4:
        book = input("Enter the book title to check: ")

        if book in books:
            print(book, "is available at index", books.index(book))
        else:
            print(book, "is not available in the library.")

    elif choice == 5:
        book = input("Enter the book title: ")
        print("Occurrences of", book, "=", books.count(book))

    elif choice == 6:
        book = input("Enter the book title to remove: ")

        if book in books:
            books.remove(book)
            print(book, "removed successfully.")
        else:
            print(book, "not found in the library.")

    elif choice == 7:
        books.sort()
        print("\nBooks after sorting:")
        for i, book in enumerate(books, start=1):
            print(i, ".", book)

    elif choice == 8:
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
