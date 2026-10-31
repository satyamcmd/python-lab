"""
Program 4: Update a student's marks in the list (Update operation).
"""

students = [
    {"roll_no": 101, "name": "Aarav Sharma", "marks": 88.5},
    {"roll_no": 102, "name": "Priya Singh", "marks": 92.0},
    {"roll_no": 103, "name": "Rohan Verma", "marks": 35.0},
]


def update_marks(students, roll_no, new_marks):
    """Update: find the student by roll number and change the marks."""
    if not 0 <= new_marks <= 100:  # basic validation
        print("Marks must be between 0 and 100.")
        return False
    for s in students:
        if s["roll_no"] == roll_no:
            old = s["marks"]
            s["marks"] = new_marks  # change the value in the record
            print(f"Marks of {s['name']} (Roll {roll_no}) updated: {old} -> {new_marks}")
            return True
    print(f"No student found with roll number {roll_no}.")
    return False


try:
    update_marks(students, 103, 58.0)   # existing student
    update_marks(students, 999, 70.0)   # roll number not in list
    update_marks(students, 101, 150)    # invalid marks
    print("\nFinal list:")
    for s in students:
        print(s)
except (KeyError, TypeError) as e:
    print("Error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Marks of Rohan Verma (Roll 103) updated: 35.0 -> 58.0
# No student found with roll number 999.
# Marks must be between 0 and 100.
#
# Final list:
# {'roll_no': 101, 'name': 'Aarav Sharma', 'marks': 88.5}
# {'roll_no': 102, 'name': 'Priya Singh', 'marks': 92.0}
# {'roll_no': 103, 'name': 'Rohan Verma', 'marks': 58.0}
