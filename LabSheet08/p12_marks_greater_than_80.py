"""
Program 12: Retrieve records where marks are greater than 80.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # WHERE clause with a parameter (?) for the condition value
    cursor.execute("SELECT id, name, age, marks FROM students WHERE marks > ?", (80,))
    rows = cursor.fetchall()

    if rows:
        print("Students with marks greater than 80:")
        print(f"{'ID':<5}{'Name':<20}{'Age':<6}{'Marks':<8}")
        print("-" * 39)
        for student_id, name, age, marks in rows:
            print(f"{student_id:<5}{name:<20}{age:<6}{marks:<8}")
    else:
        print("No student has marks greater than 80.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
