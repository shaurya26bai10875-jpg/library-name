"""
test_library.py
----------------
Basic unit tests for the core library logic in modules/book_operations.py.

Run with:  python -m unittest tests/test_library.py
(run this command from the project's root folder)
"""

import unittest
import sys
import os

# Allow importing modules/ from the project root when running this file directly
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from modules import book_operations as ops


class TestBookOperations(unittest.TestCase):

    def setUp(self):
        """Runs before every test: start with a fresh, empty library."""
        self.books = []

    def test_add_book(self):
        book = ops.add_book(self.books, "1984", "George Orwell")
        self.assertEqual(len(self.books), 1)
        self.assertEqual(book["title"], "1984")
        self.assertEqual(book["borrower"], "")

    def test_issue_available_book(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        success, message = ops.issue_book(self.books, 1, "Sepia")
        self.assertTrue(success)
        self.assertEqual(self.books[0]["borrower"], "Sepia")

    def test_issue_already_issued_book(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        ops.issue_book(self.books, 1, "Sepia")
        success, message = ops.issue_book(self.books, 1, "Rahul")
        self.assertFalse(success)
        self.assertEqual(self.books[0]["borrower"], "Sepia")  # unchanged

    def test_issue_nonexistent_book(self):
        success, message = ops.issue_book(self.books, 99, "Sepia")
        self.assertFalse(success)
        self.assertEqual(message, "Book not found.")

    def test_return_issued_book(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        ops.issue_book(self.books, 1, "Sepia")
        success, message = ops.return_book(self.books, 1)
        self.assertTrue(success)
        self.assertEqual(self.books[0]["borrower"], "")

    def test_return_book_not_issued(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        success, message = ops.return_book(self.books, 1)
        self.assertFalse(success)

    def test_search_books(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        ops.add_book(self.books, "1984", "George Orwell")
        results = ops.search_books(self.books, "dune")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Dune")

    def test_get_available_and_issued_books(self):
        ops.add_book(self.books, "Dune", "Frank Herbert")
        ops.add_book(self.books, "1984", "George Orwell")
        ops.issue_book(self.books, 1, "Sepia")

        available = ops.get_available_books(self.books)
        issued = ops.get_issued_books(self.books)

        self.assertEqual(len(available), 1)
        self.assertEqual(len(issued), 1)
        self.assertEqual(available[0]["title"], "1984")
        self.assertEqual(issued[0]["title"], "Dune")


if __name__ == "__main__":
    unittest.main()
