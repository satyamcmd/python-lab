"""
Program 24: Find the average marks of all students.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # AVG() ignores NULL values; returns None if the table is empty
    cursor.execute("SELECT AVG(marks) FROM students")
    average = cursor.fetchone()[0]

    if average is None:
        print("No records found, average cannot be calculated.")
    else:
        print(f"Average marks of all students: {average:.2f}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
