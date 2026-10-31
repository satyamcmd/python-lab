"""
Program 4: Describe the structure of the students table.

SQLite uses PRAGMA table_info (MySQL equivalent: DESCRIBE students).
"""
import sqlite3
from db_config import DB_PATH, create_students_table

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)  # make sure the table exists

    cursor = conn.cursor()
    # Each row: (cid, name, type, notnull, default_value, primary_key)
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()

    print("Structure of table 'students':")
    print(f"{'Column':<10}{'Type':<10}{'NotNull':<9}{'Default':<9}{'PK':<4}")
    print("-" * 42)
    for cid, name, col_type, notnull, default, pk in columns:
        print(f"{name:<10}{col_type:<10}{notnull:<9}{str(default):<9}{pk:<4}")

    # ---- MySQL version ----
    # cursor.execute("DESCRIBE students")
    # for row in cursor.fetchall(): print(row)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
