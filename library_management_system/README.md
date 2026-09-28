# Library Management System (CLI)

## Overview
A command-line Python application that helps manage a small library's
book collection. It allows books to be added, issued to borrowers,
returned, and tracked in real time — all data is saved to a local JSON
file after every change, so nothing is lost between runs.

## Features
- **Add books** — record a new book's title and author.
- **Issue books** — assign a book to a borrower by ID; blocks issuing a
  book that's already checked out.
- **Return books** — mark a book as available again.
- **View all books** — see the full collection with live status.
- **Search** — find books by a keyword in the title or author.
- **View available / issued books** — filtered views of the collection.
- **Persistent storage** — every add/issue/return is saved immediately to
  `data/library_data.json`, so the library's state survives a restart.
- **Input validation & error handling** — invalid menu choices, empty
  fields, and bad book IDs are caught with clear messages instead of
  crashing the program.

## Technologies / Tools Used
- Python 3 (standard library only — `json`, `os`, `unittest`)
- No external dependencies required

## Project Structure
```
library_management_system/
├── main.py                     # entry point / menu loop
├── modules/
│   ├── book_operations.py      # add, issue, return, search logic
│   ├── display.py               # menu and table printing
│   ├── storage.py               # JSON load/save (persistence)
│   └── validators.py            # input validation helpers
├── data/
│   └── library_data.json        # created automatically on first run
├── tests/
│   └── test_library.py          # unit tests for book_operations
├── README.md
└── statement.md
```

## Steps to Install & Run
1. Make sure Python 3 is installed (`python --version`).
2. Clone or download this repository.
3. From the project's root folder, run:
   ```
   python main.py
   ```
4. Follow the on-screen menu (enter a number 0–7 and press Enter).

No installation of extra packages is needed — everything uses Python's
built-in standard library.

## Instructions for Testing
Unit tests cover the core logic in `modules/book_operations.py`
(adding, issuing, returning, and searching books).

From the project's root folder, run:
```
python -m unittest tests/test_library.py -v
```
All tests should report `OK`.

## Non-Functional Requirements
- **Reliability** — data is written to disk after every change, so the
  library's state is never lost if the program closes unexpectedly.
- **Usability** — a numbered menu with clear prompts and confirmation
  messages after each action.
- **Maintainability** — logic is split into small, single-purpose
  modules (`storage`, `book_operations`, `display`, `validators`)
  instead of one large script.
- **Error handling** — every user input (menu choice, book ID, empty
  text fields) is validated before use; file read/write errors are
  caught instead of crashing the program.
- **Scalability** — the JSON-based storage layer is isolated in
  `storage.py`, so it could be swapped for a real database later
  without changing the rest of the program.

## Future Enhancements
- Due dates and overdue-book tracking
- Multiple copies per title
- A simple GUI or web front end
- Export the collection to CSV/PDF reports
