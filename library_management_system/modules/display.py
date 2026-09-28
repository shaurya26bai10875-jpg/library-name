"""
display.py
----------
Everything related to showing information to the user: the menu and
formatted tables of book data. Keeping this separate from
book_operations.py means the logic can be tested without any printing.
"""


def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a new book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. View all books")
    print("5. Search for a book")
    print("6. View available books")
    print("7. View issued books")
    print("0. Exit")
    print("======================================")


def show_books_table(books):
    """Print a list of books as a simple formatted table."""
    if not books:
        print("No books to display.")
        return

    print(f"{'ID':<4}{'Title':<25}{'Author':<20}{'Status':<20}")
    print("-" * 69)
    for book in books:
        status = f"Issued to {book['borrower']}" if book["borrower"] != "" else "Available"
        print(f"{book['id']:<4}{book['title']:<25}{book['author']:<20}{status:<20}")
