"""
Program 22: INNER JOIN between students and courses.

INNER JOIN returns only students who have at least one matching course.
"""
import sqlite3
from db_config import DB_PATH, ensure_students, ensure_courses

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    ensure_courses(conn)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT students.id, students.name, courses.course_name
        FROM students
        INNER JOIN courses ON students.id = courses.student_id
        ORDER BY students.id
        """
    )

    print("INNER JOIN result (students having courses):")
    print(f"{'ID':<5}{'Name':<20}{'Course':<25}")
    print("-" * 50)
    for student_id, name, course in cursor.fetchall():
        print(f"{student_id:<5}{name:<20}{course:<25}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
