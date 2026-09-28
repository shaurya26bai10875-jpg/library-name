# Problem Statement

Small libraries — a school reading room, a hostel common room, a
personal book collection shared with friends — are often still tracked
on paper or not tracked at all. It becomes hard to know which books
exist, who currently has a given book, and which books are free to
lend. This leads to lost books, duplicate purchases, and disputes over
who borrowed what.

## Scope
This project is a command-line Python application that digitizes the
core day-to-day operations of a small library:
- Maintaining a catalog of books
- Issuing a book to a borrower
- Recording when a book is returned
- Viewing the current status of the whole collection (available vs.
  issued) at any time

The scope is intentionally limited to a single-library, single-user
CLI tool with local JSON storage — it does not cover multi-branch
libraries, fines/fees, reservations, or a network/multi-user backend.
These are listed as future enhancements in the README.

## Target Users
- Librarians or volunteers managing a small library, classroom, or
  reading room
- Hostel/dorm common-room book collections
- Individuals who lend out personal books and want a simple, reliable
  way to track who has what

## High-Level Features
1. **Book cataloging** — add new books with a title and author; each
   book gets a unique, auto-generated ID.
2. **Issuing** — assign an available book to a named borrower; the
   system prevents issuing a book that is already checked out.
3. **Returning** — mark an issued book as available again.
4. **Real-time tracking** — every change is saved to disk immediately,
   so the collection's status is always up to date, even after
   restarting the program.
5. **Search & filtered views** — look up books by keyword, or list
   only available or only issued books.
6. **Input validation** — the system rejects invalid menu choices,
   empty inputs, and non-existent book IDs with a clear message rather
   than crashing.
