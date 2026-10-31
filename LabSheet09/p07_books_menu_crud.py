"""
Program 7: Menu-driven CRUD on a list of books (Add, View, Update, Delete).

Each book is a dictionary: {"id", "title", "author", "price"}.
"""

books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "price": 599.0},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "price": 499.0},
]


def read_int(prompt):
    """Ask until the user enters a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt):
    """Ask until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def find_book(book_id):
    """Return the book with the given id, or None."""
    for b in books:
        if b["id"] == book_id:
            return b
    return None


def add_book():
    """Create: add a new book."""
    book_id = read_int("Book ID: ")
    if find_book(book_id):
        print("A book with this ID already exists.")
        return
    title = input("Title : ").strip()
    author = input("Author: ").strip()
    price = read_float("Price : ")
    books.append({"id": book_id, "title": title, "author": author, "price": price})
    print("Book added successfully.")


def view_books():
    """Read: show all books."""
    if not books:
        print("No books available.")
        return
    print(f"\n{'ID':<5}{'Title':<30}{'Author':<18}{'Price':<8}")
    print("-" * 61)
    for b in books:
        print(f"{b['id']:<5}{b['title']:<30}{b['author']:<18}{b['price']:<8}")


def update_book():
    """Update: change title/author/price (Enter keeps the old value)."""
    book = find_book(read_int("Enter Book ID to update: "))
    if not book:
        print("Book not found.")
        return
    title = input(f"New title [{book['title']}]: ").strip()
    author = input(f"New author [{book['author']}]: ").strip()
    price = input(f"New price [{book['price']}]: ").strip()
    if title:
        book["title"] = title
    if author:
        book["author"] = author
    if price:
        try:
            book["price"] = float(price)
        except ValueError:
            print("Invalid price, old price kept.")
    print("Book updated successfully.")


def delete_book():
    """Delete: remove a book by ID."""
    book = find_book(read_int("Enter Book ID to delete: "))
    if book:
        books.remove(book)
        print("Book deleted successfully.")
    else:
        print("Book not found.")


def main():
    while True:
        print("\n===== BOOK MANAGEMENT =====")
        print("1. Add book\n2. View books\n3. Update book\n4. Delete book\n5. Exit")
        try:
            choice = input("Enter your choice (1-5): ").strip()
        except EOFError:
            break
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1 to 5.")


if __name__ == "__main__":
    main()


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Sample input typed by the user (one value per line):
#   2 | 1 | 3 | Python Basics | John Doe | 450 | 2 | 3 | 1 | Python Crash Course 3rd Ed | <Enter> | <Enter> | 4 | 2 | 2 | 5
#
# Output:
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5):
# ID   Title                         Author            Price
# -------------------------------------------------------------
# 1    Python Crash Course           Eric Matthes      599.0
# 2    Automate the Boring Stuff     Al Sweigart       499.0
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5): Book ID: Title : Author: Price : Book added successfully.
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5):
# ID   Title                         Author            Price
# -------------------------------------------------------------
# 1    Python Crash Course           Eric Matthes      599.0
# 2    Automate the Boring Stuff     Al Sweigart       499.0
# 3    Python Basics                 John Doe          450.0
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5): Enter Book ID to update: New title [Python Crash Course]: New author [Eric Matthes]: New price [599.0]: Book updated successfully.
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5): Enter Book ID to delete: Book deleted successfully.
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5):
# ID   Title                         Author            Price
# -------------------------------------------------------------
# 1    Python Crash Course 3rd Ed    Eric Matthes      599.0
# 3    Python Basics                 John Doe          450.0
#
# ===== BOOK MANAGEMENT =====
# 1. Add book
# 2. View books
# 3. Update book
# 4. Delete book
# 5. Exit
# Enter your choice (1-5): Goodbye!
