"""
Program 13: Retrieve data sorted by marks in descending order.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # ORDER BY ... DESC sorts from highest to lowest
    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY marks DESC")

    print("Students sorted by marks (highest first):")
    print(f"{'ID':<5}{'Name':<20}{'Age':<6}{'Marks':<8}")
    print("-" * 39)
    for student_id, name, age, marks in cursor.fetchall():
        print(f"{student_id:<5}{name:<20}{age:<6}{marks:<8}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
