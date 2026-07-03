from library_utils import find_book, log_activity, summarize_library

books = []


# Add a new book
def add_book(title, author):
    books.append({
        "title": title,
        "author": author,
        "available": True
    })
    print("Book added successfully.")


# Display all books
def list_books():

    if not books:
        print("No books available.")
        return

    print("\n===== Book List =====")

    for book in books:
        status = "Available" if book["available"] else "Borrowed"

        print(f"{book['title']} by {book['author']} - {status}")


# Borrow a book
def borrow_book(title):

    book = find_book(books, title)

    if book:

        if book["available"]:
            book["available"] = False
            log_activity("BORROWED", title)
            print("Book borrowed successfully.")

        else:
            print("Book is already borrowed.")

    else:
        print("Book not found.")


# Return a book
def return_book(title):

    book = find_book(books, title)

    if book:

        if not book["available"]:
            book["available"] = True
            log_activity("RETURNED", title)
            print("Book returned successfully.")

        else:
            print("Book was not borrowed.")

    else:
        print("Book not found.")


# View Borrow Log
def view_log():

    print("\n===== Borrow Log =====")

    try:
        with open("borrow_log.txt", "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("No borrow history available.")


# ---------------- MAIN PROGRAM ---------------- #

while True:

    print("\n===== CAMPUS LIB =====")
    print("1. Add Book")
    print("2. List Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Borrow Log")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        add_book(title, author)

    elif choice == "2":
        list_books()

    elif choice == "3":
        title = input("Enter book title: ")
        borrow_book(title)

    elif choice == "4":
        title = input("Enter book title: ")
        return_book(title)

    elif choice == "5":
        view_log()

    elif choice == "6":

        summarize_library(
            Total_Books=len(books),
            Available=sum(book["available"] for book in books),
            Borrowed=sum(not book["available"] for book in books)
        )

        print("Thank you for using CampusLib.")
        break

    else:
        print("Invalid choice.")