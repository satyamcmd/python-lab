"""
Program 20: Menu-driven application for all CRUD operations using a database.

Uses table students(roll_no, name, age, marks) in student_db.db.
"""
import sqlite3
from db_config import DB_PATH, create_students_table


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


def add_student(conn):
    """Create: insert a new student."""
    roll_no = read_int("Roll No: ")
    name = input("Name   : ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age = read_int("Age    : ")
    marks = read_float("Marks  : ")
    try:
        conn.execute(
            "INSERT INTO students (roll_no, name, age, marks) VALUES (?, ?, ?, ?)",
            (roll_no, name, age, marks),
        )
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print(f"Roll number {roll_no} already exists.")


def view_students(conn):
    """Read: show all students."""
    rows = conn.execute(
        "SELECT roll_no, name, age, marks FROM students ORDER BY roll_no"
    ).fetchall()
    if not rows:
        print("No student records found.")
        return
    print(f"\n{'Roll No':<10}{'Name':<20}{'Age':<6}{'Marks':<8}")
    print("-" * 44)
    for roll_no, name, age, marks in rows:
        print(f"{roll_no:<10}{name:<20}{age:<6}{marks:<8}")
    print(f"Total records: {len(rows)}")


def search_student(conn):
    """Read: find one student by roll number."""
    roll_no = read_int("Enter roll number to search: ")
    row = conn.execute(
        "SELECT roll_no, name, age, marks FROM students WHERE roll_no = ?", (roll_no,)
    ).fetchone()
    if row:
        print(f"Found: Roll {row[0]} | {row[1]} | Age {row[2]} | Marks {row[3]}")
    else:
        print("No student found with that roll number.")


def update_student(conn):
    """Update: change name and/or marks (Enter keeps the old value)."""
    roll_no = read_int("Enter roll number to update: ")
    row = conn.execute(
        "SELECT name, marks FROM students WHERE roll_no = ?", (roll_no,)
    ).fetchone()
    if row is None:
        print("No student found with that roll number.")
        return
    name = input(f"New name [{row[0]}]: ").strip()
    marks_text = input(f"New marks [{row[1]}]: ").strip()
    try:
        new_marks = float(marks_text) if marks_text else row[1]
    except ValueError:
        print("Invalid marks. Update cancelled.")
        return
    conn.execute(
        "UPDATE students SET name = ?, marks = ? WHERE roll_no = ?",
        (name if name else row[0], new_marks, roll_no),
    )
    conn.commit()
    print("Student updated successfully.")


def delete_student(conn):
    """Delete: remove a student by roll number."""
    roll_no = read_int("Enter roll number to delete: ")
    cursor = conn.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    if cursor.rowcount:
        print("Student deleted successfully.")
    else:
        print("No student found with that roll number.")


def main():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        create_students_table(conn)

        while True:
            print("\n===== STUDENT DATABASE CRUD =====")
            print("1. Add student\n2. View all students\n3. Search by roll number")
            print("4. Update student\n5. Delete student\n6. Exit")
            try:
                choice = input("Enter your choice (1-6): ").strip()
            except EOFError:
                break
            try:
                if choice == "1":
                    add_student(conn)
                elif choice == "2":
                    view_students(conn)
                elif choice == "3":
                    search_student(conn)
                elif choice == "4":
                    update_student(conn)
                elif choice == "5":
                    delete_student(conn)
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice, please enter 1 to 6.")
            except sqlite3.Error as e:
                conn.rollback()
                print("Database error:", e)
    except sqlite3.Error as e:
        print("Connection error:", e)
    finally:
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    main()


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Sample input typed by the user (one value per line):
#   2 | 1 | 101 | Aarav Sharma | 20 | 88.5 | 1 | 102 | Priya Singh | 21 | 92 | 1 | 101 | Dup | 20 | 50 | 2 | 3 | 102 | 4 | 101 | <Enter> | 91 | 5 | 102 | 2 | 6
#
# Output:
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): No student records found.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Roll No: Name   : Age    : Marks  : Student added successfully.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Roll No: Name   : Age    : Marks  : Student added successfully.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Roll No: Name   : Age    : Marks  : Roll number 101 already exists.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6):
# Roll No   Name                Age   Marks
# --------------------------------------------
# 101       Aarav Sharma        20    88.5
# 102       Priya Singh         21    92.0
# Total records: 2
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Enter roll number to search: Found: Roll 102 | Priya Singh | Age 21 | Marks 92.0
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Enter roll number to update: New name [Aarav Sharma]: New marks [88.5]: Student updated successfully.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Enter roll number to delete: Student deleted successfully.
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6):
# Roll No   Name                Age   Marks
# --------------------------------------------
# 101       Aarav Sharma        20    91.0
# Total records: 1
#
# ===== STUDENT DATABASE CRUD =====
# 1. Add student
# 2. View all students
# 3. Search by roll number
# 4. Update student
# 5. Delete student
# 6. Exit
# Enter your choice (1-6): Goodbye!
# Connection closed.
