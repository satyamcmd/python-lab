"""
Program 1: Connect to a database and display a success message.

SQLite is used (built into Python). MySQL equivalent is shown in comments.
"""
import sqlite3
from db_config import DB_PATH

conn = None
try:
    # Connect to the database file (it is created automatically if missing)
    conn = sqlite3.connect(DB_PATH)
    print("Connection to database successful!")
    print("SQLite version:", sqlite3.sqlite_version)

    # ---- MySQL version (needs: pip install mysql-connector-python) ----
    # import mysql.connector
    # conn = mysql.connector.connect(host="localhost", user="root",
    #                                password="your_password")
    # if conn.is_connected():
    #     print("Connection to MySQL successful!")
except sqlite3.Error as e:
    # Handle connection errors
    print("Connection failed:", e)
finally:
    # Always close the connection
    if conn:
        conn.close()
        print("Connection closed.")
