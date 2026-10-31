"""
Program 12: Insert a new record into the students table (Create operation).

Change the values below to add a different student.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

ROLL_NO, NAME, AGE, MARKS = 106, "Sneha Reddy", 21, 85.5

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    # Parameterized query (?) keeps the data safe from SQL injection
    conn.execute(
        "INSERT INTO students (roll_no, name, age, marks) VALUES (?, ?, ?, ?)",
        (ROLL_NO, NAME, AGE, MARKS),
    )
    conn.commit()
    print(f"Student '{NAME}' (Roll No {ROLL_NO}) added successfully.")
except sqlite3.IntegrityError:
    # Raised when the roll number already exists
    print(f"Error: Roll number {ROLL_NO} already exists. Record not added.")
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
# Student 'Sneha Reddy' (Roll No 106) added successfully.
# Connection closed.
