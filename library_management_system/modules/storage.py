"""
storage.py
----------
Handles reading and writing the library's data to a JSON file so that
book records, issue status, and borrower details are preserved between
program runs (this is what makes tracking "real time" / persistent).
"""

import json
import os


def load_books(filepath):
    """
    Load the list of books from the JSON file at filepath.
    Returns an empty list if the file does not exist yet or is empty/corrupt.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r") as file:
            content = file.read().strip()
            if content == "":
                return []
            return json.loads(content)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: could not read data file ({error}). Starting with an empty library.")
        return []


def save_books(books, filepath):
    """
    Save the current list of books to the JSON file at filepath.
    Creates the containing folder if it does not exist.
    Returns True on success, False on failure.
    """
    try:
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(filepath, "w") as file:
            json.dump(books, file, indent=4)
        return True
    except OSError as error:
        print(f"Error: could not save data ({error}).")
        return False
