"""
Program 16: Update the marks of a student using their ID.

Change STUDENT_ID and NEW_MARKS below to try other values.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

STUDENT_ID = 3
NEW_MARKS = 55.0

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (NEW_MARKS, STUDENT_ID))
    conn.commit()

    # rowcount tells how many rows were changed
    if cursor.rowcount:
        print(f"Marks of student ID {STUDENT_ID} updated to {NEW_MARKS}.")
    else:
        print(f"No student found with ID {STUDENT_ID}.")
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
