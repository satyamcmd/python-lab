"""
Program 13: Read and display all records from the table (Read operation).
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    rows = conn.execute("SELECT roll_no, name, age, marks FROM students").fetchall()

    if rows:
        print(f"{'Roll No':<10}{'Name':<20}{'Age':<6}{'Marks':<8}")
        print("-" * 44)
        for roll_no, name, age, marks in rows:
            print(f"{roll_no:<10}{name:<20}{age:<6}{marks:<8}")
    else:
        print("The students table is empty.")
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
# Roll No   Name                Age   Marks
# --------------------------------------------
# 101       Aarav Sharma        20    88.5
# 102       Priya Singh         21    92.0
# 103       Rohan Verma         20    35.0
# 104       Neha Gupta          22    76.5
# 105       Kabir Khan          21    81.0
# 106       Sneha Reddy         21    85.5
# Connection closed.
