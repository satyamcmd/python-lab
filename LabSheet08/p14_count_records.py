"""
Program 14: Count the total number of records in the students table.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # COUNT(*) returns a single row with a single value
    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    print("Total number of records in 'students':", total)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
