"""
Program 2: Create a new database (student_db).

In SQLite, a database is a file: connecting to a new file name creates it.
MySQL equivalent: CREATE DATABASE student_db  (shown in comments).
"""
import os
import sqlite3
from db_config import DB_PATH, DB_NAME

conn = None
try:
    existed = os.path.exists(DB_PATH)

    # Connecting creates the database file if it does not exist
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA user_version = 1")  # forces the file to be written
    conn.commit()

    if existed:
        print(f"Database '{DB_NAME}' already exists at: {DB_PATH}")
    else:
        print(f"Database '{DB_NAME}' created successfully at: {DB_PATH}")

    # ---- MySQL version ----
    # cursor = conn.cursor()
    # cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    # cursor.execute("SHOW DATABASES")
    # for (db,) in cursor: print(db)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
