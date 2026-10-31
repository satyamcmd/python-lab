"""
Program 14: Search for a specific student by roll number.

Change SEARCH_ROLL to look up another student.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

SEARCH_ROLL = 102

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    # fetchone() returns one row, or None when nothing matches
    row = conn.execute(
        "SELECT roll_no, name, age, marks FROM students WHERE roll_no = ?",
        (SEARCH_ROLL,),
    ).fetchone()

    if row:
        print("Student found:")
        print(f"  Roll No : {row[0]}")
        print(f"  Name    : {row[1]}")
        print(f"  Age     : {row[2]}")
        print(f"  Marks   : {row[3]}")
    else:
        print(f"No student found with roll number {SEARCH_ROLL}.")
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
# Student found:
#   Roll No : 102
#   Name    : Priya Singh
#   Age     : 21
#   Marks   : 92.0
# Connection closed.
