"""
main.py
-------
Entry point for the Library Management System.

Run with:  python main.py

This file only handles the menu loop and user interaction. All the
real logic lives in modules/book_operations.py, modules/storage.py
and modules/display.py, so the program is easy to read, test, and
extend.
"""

from modules import storage
from modules import book_operations as ops
from modules import display
from modules import validators

DATA_FILE = "data/library_data.json"
VALID_CHOICES = ["0", "1", "2", "3", "4", "5", "6", "7"]


def main():
    books = storage.load_books(DATA_FILE)
    print("Library data loaded. Welcome!")

    while True:
        display.show_menu()
        choice = input("Enter choice: ").strip()

        if not validators.is_valid_menu_choice(choice, VALID_CHOICES):
            print("Invalid choice. Please enter a number from 0 to 7.")
            continue

        if choice == "1":
            handle_add_book(books)

        elif choice == "2":
            handle_issue_book(books)

        elif choice == "3":
            handle_return_book(books)

        elif choice == "4":
            display.show_books_table(books)

        elif choice == "5":
            handle_search(books)

        elif choice == "6":
            display.show_books_table(ops.get_available_books(books))

        elif choice == "7":
            display.show_books_table(ops.get_issued_books(books))

        elif choice == "0":
            storage.save_books(books, DATA_FILE)
            print("Data saved. Goodbye!")
            break


def handle_add_book(books):
    title = input("Book title: ").strip()
    author = input("Author name: ").strip()

    if not validators.is_non_empty(title) or not validators.is_non_empty(author):
        print("Title and author cannot be empty. Book not added.")
        return

    new_book = ops.add_book(books, title, author)
    storage.save_books(books, DATA_FILE)
    print(f'Book added: "{new_book["title"]}" (ID {new_book["id"]}).')


def handle_issue_book(books):
    if not books:
        print("No books in the library yet.")
        return

    book_id_text = input("Enter the ID of the book to issue: ").strip()
    if not validators.is_valid_book_id(book_id_text, len(books)):
        print("Invalid book ID.")
        return

    borrower_name = input("Borrower's name: ").strip()
    if not validators.is_non_empty(borrower_name):
        print("Borrower name cannot be empty. Book not issued.")
        return

    success, message = ops.issue_book(books, int(book_id_text), borrower_name)
    print(message)
    if success:
        storage.save_books(books, DATA_FILE)


def handle_return_book(books):
    if not books:
        print("No books in the library yet.")
        return

    book_id_text = input("Enter the ID of the book to return: ").strip()
    if not validators.is_valid_book_id(book_id_text, len(books)):
        print("Invalid book ID.")
        return

    success, message = ops.return_book(books, int(book_id_text))
    print(message)
    if success:
        storage.save_books(books, DATA_FILE)


def handle_search(books):
    keyword = input("Enter a title or author keyword to search: ").strip()
    if not validators.is_non_empty(keyword):
        print("Please enter something to search for.")
        return

    results = ops.search_books(books, keyword)
    if not results:
        print("No matching books found.")
    else:
        display.show_books_table(results)


if __name__ == "__main__":
    main()
