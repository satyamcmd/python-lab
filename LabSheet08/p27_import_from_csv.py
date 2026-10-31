"""
Program 27: Import data from a CSV file into a database table.

Expected CSV header: name,age,marks   (id is generated automatically)
If students_import.csv does not exist, a sample file is created first.
"""
import csv
import os
import sqlite3
from db_config import DB_PATH, create_students_table

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students_import.csv")

# Create a sample CSV when the file is missing so the program can be tested
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "marks"])
        writer.writerows([
            ("Meera Joshi", 20, 79.5),
            ("Arjun Nair", 22, 91.0),
            ("Divya Mishra", 21, 58.0),
        ])
    print("Sample file 'students_import.csv' created.")

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    create_students_table(conn)
    cursor = conn.cursor()

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # reads each row as a dictionary
        data = [(row["name"], int(row["age"]), float(row["marks"])) for row in reader]

    cursor.executemany(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", data
    )
    conn.commit()
    print(f"{len(data)} records imported from CSV into 'students'.")
except FileNotFoundError:
    print("CSV file not found:", CSV_FILE)
except (KeyError, ValueError) as e:
    conn.rollback() if conn else None
    print("CSV format error:", e)
except sqlite3.Error as e:
    conn.rollback() if conn else None
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
