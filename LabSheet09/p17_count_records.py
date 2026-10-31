"""
Program 17: Count and display the total number of records in the table.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    # COUNT(*) returns one row holding the number of records
    total = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total number of student records:", total)
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
# Total number of student records: 5
# Connection closed.
