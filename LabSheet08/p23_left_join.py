"""
Program 23: LEFT JOIN between students and courses.

LEFT JOIN returns ALL students; students without a course show None (NULL).
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
        LEFT JOIN courses ON students.id = courses.student_id
        ORDER BY students.id
        """
    )

    print("LEFT JOIN result (all students):")
    print(f"{'ID':<5}{'Name':<20}{'Course':<25}")
    print("-" * 50)
    for student_id, name, course in cursor.fetchall():
        # Replace NULL with a readable text
        print(f"{student_id:<5}{name:<20}{course if course else '-- no course --':<25}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
