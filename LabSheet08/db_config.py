"""
db_config.py - shared settings and helpers for all Lab Sheet-08 programs.

All programs use ONE common database file: student_db.db (SQLite).
Keep this file in the same folder as the other programs.
"""
import os
import sqlite3

# Common database used by every program (created in this folder)
DB_NAME = "student_db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME + ".db")

# Sample data used to seed the tables so every program can run on its own
SAMPLE_STUDENTS = [
    ("Aarav Sharma", 20, 88.5),
    ("Priya Singh", 21, 92.0),
    ("Rohan Verma", 20, 35.0),
    ("Neha Gupta", 22, 76.5),
    ("Kabir Khan", 21, 81.0),
    ("Isha Patel", 22, 67.0),
]

SAMPLE_COURSES = [
    (1, "Python Programming"),
    (1, "Data Structures"),
    (2, "Database Systems"),
    (4, "Operating Systems"),
    (5, "Computer Networks"),
]


def get_connection():
    """Return a new connection to the common database."""
    return sqlite3.connect(DB_PATH)


def create_students_table(conn):
    """Create the students table if it does not exist (no data added)."""
    conn.execute(
        """CREATE TABLE IF NOT EXISTS students (
               id    INTEGER PRIMARY KEY AUTOINCREMENT,
               name  TEXT    NOT NULL,
               age   INTEGER,
               marks REAL
           )"""
    )
    conn.commit()


def ensure_students(conn):
    """Make sure the students table exists AND has sample rows."""
    create_students_table(conn)
    count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
            SAMPLE_STUDENTS,
        )
        conn.commit()


def ensure_courses(conn):
    """Make sure the courses table exists AND has sample rows."""
    conn.execute(
        """CREATE TABLE IF NOT EXISTS courses (
               course_id   INTEGER PRIMARY KEY AUTOINCREMENT,
               student_id  INTEGER,
               course_name TEXT NOT NULL,
               FOREIGN KEY (student_id) REFERENCES students(id)
           )"""
    )
    count = conn.execute("SELECT COUNT(*) FROM courses").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO courses (student_id, course_name) VALUES (?, ?)",
            SAMPLE_COURSES,
        )
    conn.commit()
