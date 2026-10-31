"""
Program 20: Truncate (empty) a table while keeping its structure intact.

SQLite has no TRUNCATE command, so we use DELETE FROM and reset the
auto-increment counter. MySQL equivalent: TRUNCATE TABLE students
"""
import sqlite3
from db_config import DB_PATH, create_students_table

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)
    cursor = conn.cursor()

    # Remove every row but keep the table definition
    cursor.execute("DELETE FROM students")
    # Reset the id counter so the next insert starts from 1 again
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = ?", ("students",))
    conn.commit()
    print("Table 'students' truncated. All rows removed, structure kept.")

    # Prove the structure is still there
    cursor.execute("SELECT COUNT(*) FROM students")
    print("Rows remaining:", cursor.fetchone()[0])
    cursor.execute("PRAGMA table_info(students)")
    print("Columns still present:", [col[1] for col in cursor.fetchall()])
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
