"""
Program 11: Display only specific columns (name and marks).
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # Select only the columns we need instead of SELECT *
    cursor.execute("SELECT name, marks FROM students")

    print(f"{'Name':<20}{'Marks':<8}")
    print("-" * 28)
    for name, marks in cursor.fetchall():
        print(f"{name:<20}{marks:<8}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
