"""
Program 17: Update the name of a student.

Change STUDENT_ID and NEW_NAME below to try other values.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

STUDENT_ID = 1
NEW_NAME = "Aarav Kumar Sharma"

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (NEW_NAME, STUDENT_ID))
    conn.commit()

    if cursor.rowcount:
        print(f"Name of student ID {STUDENT_ID} updated to '{NEW_NAME}'.")
    else:
        print(f"No student found with ID {STUDENT_ID}.")
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
