"""
Program 15: Update the marks of a student using roll number (Update operation).

Change ROLL_NO and NEW_MARKS to update another student.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

ROLL_NO = 103
NEW_MARKS = 58.0

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    cursor = conn.execute(
        "UPDATE students SET marks = ? WHERE roll_no = ?", (NEW_MARKS, ROLL_NO)
    )
    conn.commit()

    # rowcount = number of rows changed (0 means the roll number was not found)
    if cursor.rowcount:
        print(f"Marks of Roll No {ROLL_NO} updated to {NEW_MARKS}.")
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
# Marks of Roll No 103 updated to 58.0.
# Connection closed.
