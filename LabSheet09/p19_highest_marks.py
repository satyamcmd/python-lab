"""
Program 19: Find the student with the highest marks from the database.

If several students share the highest marks, all of them are shown.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    # The subquery finds the maximum marks; the outer query returns who has it
    rows = conn.execute(
        """
        SELECT roll_no, name, age, marks FROM students
        WHERE marks = (SELECT MAX(marks) FROM students)
        """
    ).fetchall()

    if rows:
        print("Student(s) with the highest marks:")
        for roll_no, name, age, marks in rows:
            print(f"  Roll No {roll_no} | {name} | Age {age} | Marks {marks}")
    else:
        print("No records found.")
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
# Student(s) with the highest marks:
#   Roll No 102 | Priya Singh | Age 21 | Marks 92.0
# Connection closed.
