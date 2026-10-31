"""
db_config.py - shared settings for the database programs (11 to 20).

All programs use one SQLite database file (student_db.db) and a table
students(roll_no, name, age, marks). Keep this file in the same folder.
"""
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_db.db")

SAMPLE_STUDENTS = [
    (101, "Aarav Sharma", 20, 88.5),
    (102, "Priya Singh", 21, 92.0),
    (103, "Rohan Verma", 20, 35.0),
    (104, "Neha Gupta", 22, 76.5),
    (105, "Kabir Khan", 21, 81.0),
]


def create_students_table(conn):
    """Create the students table if it does not exist (no data added)."""
    conn.execute(
        """CREATE TABLE IF NOT EXISTS students (
               roll_no INTEGER PRIMARY KEY,
               name    TEXT NOT NULL,
               age     INTEGER,
               marks   REAL
           )"""
    )
    conn.commit()


def ensure_students(conn):
    """Create the table and add sample rows if the table is empty."""
    create_students_table(conn)
    if conn.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 0:
        conn.executemany(
            "INSERT INTO students (roll_no, name, age, marks) VALUES (?, ?, ?, ?)",
            SAMPLE_STUDENTS,
        )
        conn.commit()
