"""
Program 25: Display students grouped by age and count how many are in each group.
"""
import sqlite3
from db_config import DB_PATH, ensure_students

conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)
    cursor = conn.cursor()

    # GROUP BY collects rows with the same age; COUNT(*) counts each group
    cursor.execute(
        "SELECT age, COUNT(*) FROM students GROUP BY age ORDER BY age"
    )

    print(f"{'Age':<8}{'Number of Students':<20}")
    print("-" * 28)
    for age, count in cursor.fetchall():
        print(f"{age:<8}{count:<20}")

    # Bonus: show the student names inside each age group
    print("\nStudents in each age group:")
    cursor.execute(
        "SELECT age, GROUP_CONCAT(name, ', ') FROM students GROUP BY age ORDER BY age"
    )
    for age, names in cursor.fetchall():
        print(f"  Age {age}: {names}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()
        print("Connection closed.")
