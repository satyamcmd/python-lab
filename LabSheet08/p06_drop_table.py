"""
Program 6: Drop (delete) a table from the database.

To keep the 'students' data safe for other programs, this demo first creates a
temporary table called 'temp_table' and then drops it.
Change TABLE_TO_DROP to drop any other table.
"""
import sqlite3
from db_config import DB_PATH

TABLE_TO_DROP = "temp_table"

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create a demo table so there is something to drop
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_TO_DROP} (id INTEGER, note TEXT)")
    conn.commit()
    print(f"Table '{TABLE_TO_DROP}' created for demonstration.")

    # DROP TABLE IF EXISTS avoids an error when the table is missing.
    # (Table names cannot be passed as ? parameters, so it is set in code above.)
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_TO_DROP}")
    conn.commit()
    print(f"Table '{TABLE_TO_DROP}' dropped successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
