"""
Program 9: Insert multiple records into the students table.
"""
import sqlite3
from db_config import DB_PATH, create_students_table, SAMPLE_STUDENTS

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)
    cursor = conn.cursor()

    sql = "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)"

    # executemany() inserts every tuple in the list in one call
    cursor.executemany(sql, SAMPLE_STUDENTS)
    conn.commit()
    print(cursor.rowcount, "records inserted successfully.")
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
