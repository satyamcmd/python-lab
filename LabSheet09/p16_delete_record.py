"""
Program 16: Delete a student record using roll number (Delete operation).

Change ROLL_NO to delete another student.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

ROLL_NO = 105

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    cursor = conn.execute("DELETE FROM students WHERE roll_no = ?", (ROLL_NO,))
    conn.commit()

    if cursor.rowcount:
        print(f"Student with Roll No {ROLL_NO} deleted successfully.")
    else:
        print(f"No student found with roll number {ROLL_NO}.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Student with Roll No 105 deleted successfully.
# Connection closed.
