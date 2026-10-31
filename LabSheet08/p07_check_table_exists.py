"""
Program 7: Check if a specific table exists in the database.
"""
import sqlite3
from db_config import DB_PATH, create_students_table


def table_exists(cursor, table_name):
    """Return True if the table exists (parameterized query)."""
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",
        (table_name,),
    )
    return cursor.fetchone() is not None


conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)
    cursor = conn.cursor()

    # Check one table that exists and one that does not
    for name in ("students", "teachers"):
        if table_exists(cursor, name):
            print(f"Table '{name}' exists.")
        else:
            print(f"Table '{name}' does NOT exist.")

    # ---- MySQL version ----
    # cursor.execute("SHOW TABLES LIKE %s", ("students",))
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
