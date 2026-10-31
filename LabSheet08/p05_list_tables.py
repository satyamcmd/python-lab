"""
Program 5: List all tables available in the connected database.

SQLite keeps table names in sqlite_master (MySQL equivalent: SHOW TABLES).
"""
import sqlite3
from db_config import DB_PATH, create_students_table

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)  # ensure at least one table exists

    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )
    tables = cursor.fetchall()

    if tables:
        print("Tables in the database:")
        for number, (table_name,) in enumerate(tables, start=1):
            print(f"  {number}. {table_name}")
    else:
        print("No tables found in the database.")

    # ---- MySQL version ----
    # cursor.execute("SHOW TABLES")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
