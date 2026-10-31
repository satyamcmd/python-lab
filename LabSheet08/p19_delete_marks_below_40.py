"""
Program 19: Delete all students with marks below 40.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

PASS_MARKS = 40

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE marks < ?", (PASS_MARKS,))
    conn.commit()

    print(f"{cursor.rowcount} student(s) with marks below {PASS_MARKS} deleted.")
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
