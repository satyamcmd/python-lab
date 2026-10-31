"""
Program 18: Delete a student record using ID.

Change STUDENT_ID below to delete a different student.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

STUDENT_ID = 6

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (STUDENT_ID,))
    conn.commit()

    if cursor.rowcount:
        print(f"Student with ID {STUDENT_ID} deleted successfully.")
    else:
        print(f"No student found with ID {STUDENT_ID}.")
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
