"""
Program 10: Read and display all records from the students table.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)  # table + sample data if empty
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()  # list of tuples

    print(f"{'ID':<5}{'Name':<20}{'Age':<6}{'Marks':<8}")
    print("-" * 39)
    for student_id, name, age, marks in rows:
        print(f"{student_id:<5}{name:<20}{age:<6}{marks:<8}")
    print(f"\nTotal records: {len(rows)}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
