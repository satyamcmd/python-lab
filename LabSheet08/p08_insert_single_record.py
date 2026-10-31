"""
Program 8: Insert a single record into the students table.
"""
import sqlite3
from db_config import DB_PATH, create_students_table

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)
    cursor = conn.cursor()

    # Parameterized query (?) prevents SQL injection
    sql = "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)"
    record = ("Sneha Reddy", 21, 85.5)

    cursor.execute(sql, record)
    conn.commit()  # make the insert permanent
    print("1 record inserted successfully. New id =", cursor.lastrowid)
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
