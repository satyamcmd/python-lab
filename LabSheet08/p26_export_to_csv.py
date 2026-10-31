"""
Program 26: Export table data from the database into a CSV file.
"""
import csv
import os
import sqlite3
from db_config import DB_PATH, ensure_students

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students_export.csv")

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students")
    rows = cursor.fetchall()
    # cursor.description holds the column names
    headers = [col[0] for col in cursor.description]

    # newline="" avoids blank lines between rows on Windows
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)   # header row
        writer.writerows(rows)     # data rows

    print(f"{len(rows)} records exported to: {CSV_FILE}")
except sqlite3.Error as e:
    print("Database error:", e)
except OSError as e:
    print("File error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
