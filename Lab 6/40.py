books = []


def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print("Book added.")


def display_books():
    if not books:
        print("No books available.")
    else:
        for i in range(len(books)):
            print(i, "-", books[i])


def search_book(name):
    for i in range(len(books)):
        if books[i].lower() == name.lower():
            return i

    return -1


def delete_book():
    name = input("Enter book name to delete: ")
    pos = search_book(name)

    if pos == -1:
        print("Book not found.")
    else:
        books.pop(pos)
        print("Book deleted.")


while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        name = input("Enter book name to search: ")
        print("Position =", search_book(name))

    elif choice == "4":
        delete_book()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
