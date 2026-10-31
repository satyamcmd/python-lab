"""
Program 15: Display the top 3 highest scoring students.

SQLite and MySQL both support: ORDER BY marks DESC LIMIT 3
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, marks FROM students ORDER BY marks DESC LIMIT ?", (3,)
    )

    print("Top 3 highest scoring students:")
    for rank, (name, marks) in enumerate(cursor.fetchall(), start=1):
        print(f"  {rank}. {name:<20} {marks}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
