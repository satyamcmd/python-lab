"""
Program 11: Connect to a database and create the table students.

Table: students(roll_no, name, age, marks)
"""
import sqlite3
from db_config import DB_PATH

conn = None
try:
    # Connect (the database file is created if it does not exist)
    conn = sqlite3.connect(DB_PATH)
    print("Connected to database successfully.")

    # Create the table; IF NOT EXISTS avoids an error on re-run
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name    TEXT NOT NULL,
            age     INTEGER,
            marks   REAL
        )
        """
    )
    conn.commit()
    print("Table 'students' created successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()  # always close the connection
        print("Connection closed.")


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Connected to database successfully.
# Table 'students' created successfully.
# Connection closed.
