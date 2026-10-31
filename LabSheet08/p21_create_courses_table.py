"""
Program 21: Create a table for courses and insert data into it.

courses(course_id, student_id, course_name) - student_id links to students.id
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)  # courses refer to students, so make sure they exist
    cursor = conn.cursor()

    # Start fresh so re-running the program does not duplicate the data
    cursor.execute("DROP TABLE IF EXISTS courses")
    cursor.execute(
        """
        CREATE TABLE courses (
            course_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id  INTEGER,
            course_name TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
        """
    )
    print("Table 'courses' created.")

    course_data = [
        (1, "Python Programming"),
        (1, "Data Structures"),
        (2, "Database Systems"),
        (4, "Operating Systems"),
        (5, "Computer Networks"),
    ]
    cursor.executemany(
        "INSERT INTO courses (student_id, course_name) VALUES (?, ?)", course_data
    )
    conn.commit()
    print(f"{cursor.rowcount} course records inserted.")

    # Show the result
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
