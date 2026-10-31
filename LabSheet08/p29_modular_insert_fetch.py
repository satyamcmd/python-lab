"""
Program 29: Use functions to insert and fetch data (modular approach).

Each job (connect, insert, fetch, display) is a separate reusable function.
"""
import sqlite3
from db_config import DB_PATH, create_students_table


def connect():
    """Open and return a connection to the database."""
    return sqlite3.connect(DB_PATH)


def insert_student(conn, name, age, marks):
    """Insert one student and return the new id."""
    cursor = conn.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks),
    )
    conn.commit()
    return cursor.lastrowid


def fetch_students(conn):
    """Return all students as a list of tuples."""
    return conn.execute("SELECT id, name, age, marks FROM students").fetchall()


def display_students(rows):
    """Print a list of student rows as a table."""
    print(f"{'ID':<5}{'Name':<20}{'Age':<6}{'Marks':<8}")
    print("-" * 39)
    for student_id, name, age, marks in rows:
        print(f"{student_id:<5}{name:<20}{age:<6}{marks:<8}")


def main():
    conn = None
    try:
        conn = connect()
        create_students_table(conn)

        new_id = insert_student(conn, "Tanvi Rawat", 21, 84.0)
        print("Inserted student with id:", new_id)

        print("\nAll students:")
        display_students(fetch_students(conn))
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        if conn:
            conn.close()
            print("\nConnection closed.")


if __name__ == "__main__":
    main()
