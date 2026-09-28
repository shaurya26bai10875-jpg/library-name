"""
validators.py
-------------
Small helper functions that check user input before it is used,
so the rest of the program does not crash on bad input.
"""


def is_non_empty(text):
    """Return True if text has at least one non-whitespace character."""
    return text.strip() != ""


def is_valid_menu_choice(choice, valid_choices):
    """Return True if choice (as a string) is one of valid_choices."""
    return choice in valid_choices


def is_valid_book_id(book_id_text, total_books):
    """
    Check that book_id_text is a whole number that could refer to a
    real book (between 1 and total_books, inclusive).
    """
    if not book_id_text.isdigit():
        return False
    book_id = int(book_id_text)
    return 1 <= book_id <= total_books
