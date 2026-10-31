"""
Program 30: Menu-driven student management application (Add, View, Update, Delete).
"""
import sqlite3
from db_config import DB_PATH, create_students_table


def read_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt):
    """Keep asking until the user types a number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def add_student(conn):
    name = input("Name  : ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age = read_int("Age   : ")
    marks = read_float("Marks : ")
    conn.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks)
    )
    conn.commit()
    print("Student added successfully.")


def view_students(conn):
    rows = conn.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
    if not rows:
        print("No students found.")
        return
    print(f"\n{'ID':<5}{'Name':<20}{'Age':<6}{'Marks':<8}")
    print("-" * 39)
    for student_id, name, age, marks in rows:
        print(f"{student_id:<5}{name:<20}{age:<6}{marks:<8}")


def update_student(conn):
    student_id = read_int("Enter student ID to update: ")
    name = input("New name (press Enter to keep current): ").strip()
    marks_text = input("New marks (press Enter to keep current): ").strip()

    cursor = conn.execute("SELECT name, marks FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row is None:
        print("No student found with that ID.")
        return

    new_name = name if name else row[0]
    try:
        new_marks = float(marks_text) if marks_text else row[1]
    except ValueError:
        print("Invalid marks. Update cancelled.")
        return

    conn.execute(
        "UPDATE students SET name = ?, marks = ? WHERE id = ?",
        (new_name, new_marks, student_id),
    )
    conn.commit()
    print("Student updated successfully.")


def delete_student(conn):
    student_id = read_int("Enter student ID to delete: ")
    cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    if cursor.rowcount:
        print("Student deleted successfully.")
    else:
        print("No student found with that ID.")


def main():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        create_students_table(conn)

        while True:
            print("\n===== STUDENT MANAGEMENT =====")
            print("1. Add student")
            print("2. View students")
            print("3. Update student")
            print("4. Delete student")
            print("5. Exit")
            try:
                choice = input("Enter your choice (1-5): ").strip()
            except EOFError:  # input ended (e.g. piped input)
                break

            try:
                if choice == "1":
                    add_student(conn)
                elif choice == "2":
                    view_students(conn)
                elif choice == "3":
                    update_student(conn)
                elif choice == "4":
                    delete_student(conn)
                elif choice == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice, please enter 1 to 5.")
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
