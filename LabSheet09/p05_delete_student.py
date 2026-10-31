"""
Program 5: Delete a student record by roll number (Delete operation).
"""

students = [
    {"roll_no": 101, "name": "Aarav Sharma", "marks": 88.5},
    {"roll_no": 102, "name": "Priya Singh", "marks": 92.0},
    {"roll_no": 103, "name": "Rohan Verma", "marks": 35.0},
    {"roll_no": 104, "name": "Neha Gupta", "marks": 76.5},
]


def delete_student(students, roll_no):
    """Delete: remove the record with the given roll number."""
    for index, s in enumerate(students):
        if s["roll_no"] == roll_no:
            removed = students.pop(index)  # remove from the list by position
            print(f"Deleted: Roll {removed['roll_no']} - {removed['name']}")
            return True
    print(f"No student found with roll number {roll_no}.")
    return False


try:
    print("Before delete:", [s["roll_no"] for s in students])
    delete_student(students, 103)   # exists
    delete_student(students, 555)   # does not exist
    print("After delete :", [s["roll_no"] for s in students])
except (KeyError, TypeError) as e:
    print("Error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Before delete: [101, 102, 103, 104]
# Deleted: Roll 103 - Rohan Verma
# No student found with roll number 555.
# After delete : [101, 102, 104]
