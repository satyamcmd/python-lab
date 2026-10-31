"""
Program 2: Display all student records from the list (Read operation).
"""

# Sample list of student records
students = [
    {"roll_no": 101, "name": "Aarav Sharma", "marks": 88.5},
    {"roll_no": 102, "name": "Priya Singh", "marks": 92.0},
    {"roll_no": 103, "name": "Rohan Verma", "marks": 35.0},
    {"roll_no": 104, "name": "Neha Gupta", "marks": 76.5},
]


def display_students(students):
    """Read: print every record in a neat table."""
    if not students:  # empty list check
        print("No student records found.")
        return
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<8}")
    print("-" * 38)
    for s in students:  # loop through each record
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['marks']:<8}")
    print(f"\nTotal records: {len(students)}")


try:
    display_students(students)
except (KeyError, TypeError) as e:
    print("Record format error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Roll No   Name                Marks
# --------------------------------------
# 101       Aarav Sharma        88.5
# 102       Priya Singh         92.0
# 103       Rohan Verma         35.0
# 104       Neha Gupta          76.5
#
# Total records: 4
