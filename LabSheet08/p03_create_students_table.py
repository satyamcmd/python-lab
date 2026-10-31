"""
Program 3: Create a table named 'students' with columns (id, name, age, marks).
"""
import sqlite3
from db_config import DB_PATH

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # CREATE TABLE IF NOT EXISTS avoids an error if the table already exists
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            age   INTEGER,
            marks REAL
        )
        """
    )
    conn.commit()  # save the change
    print("Table 'students' created successfully (or already exists).")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
