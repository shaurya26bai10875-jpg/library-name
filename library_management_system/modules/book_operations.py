"""
book_operations.py
-------------------
The core logic of the library system: adding books, issuing them to
borrowers, returning them, and searching the collection.

Each book is stored as a dictionary:
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "borrower": ""        # empty string means the book is available
    }
"""


def add_book(books, title, author):
    """
    Add a new book to the books list and return the newly created book.
    The id is simply the next number in sequence.
    """
    new_id = len(books) + 1
    new_book = {
        "id": new_id,
        "title": title.strip(),
        "author": author.strip(),
        "borrower": ""
    }
    books.append(new_book)
    return new_book


def issue_book(books, book_id, borrower_name):
    """
    Mark the book with the given id as issued to borrower_name.
    Returns a (success, message) tuple.
    """
    for book in books:
        if book["id"] == book_id:
            if book["borrower"] == "":
                book["borrower"] = borrower_name.strip()
                return True, f'"{book["title"]}" has been issued to {borrower_name}.'
            else:
                return False, f'"{book["title"]}" is already issued to {book["borrower"]}.'
    return False, "Book not found."


def return_book(books, book_id):
    """
    Mark the book with the given id as returned (available again).
    Returns a (success, message) tuple.
    """
    for book in books:
        if book["id"] == book_id:
            if book["borrower"] != "":
                previous_borrower = book["borrower"]
                book["borrower"] = ""
                return True, f'"{book["title"]}" has been returned (was with {previous_borrower}).'
            else:
                return False, f'"{book["title"]}" was not issued to anyone.'
    return False, "Book not found."


def search_books(books, keyword):
    """
    Return a list of books whose title or author contains keyword
    (case-insensitive).
    """
    keyword = keyword.strip().lower()
    results = []
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            results.append(book)
    return results


def get_available_books(books):
    """Return a list of books that are not currently issued."""
    available = []
    for book in books:
        if book["borrower"] == "":
            available.append(book)
    return available


def get_issued_books(books):
    """Return a list of books that are currently issued."""
    issued = []
    for book in books:
        if book["borrower"] != "":
            issued.append(book)
    return issued
