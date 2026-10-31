"""
Program 1: Create a list of student records (Create operation).

Each student is a dictionary: {"roll_no", "name", "marks"}.
The list is built by adding records one at a time with add_student().
"""


def add_student(students, roll_no, name, marks):
    """Create: add one student record to the list (roll numbers must be unique)."""
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Roll number {roll_no} already exists. Record not added.")
            return
    # Build the record as a dictionary and append it to the list
    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    print(f"Student '{name}' added successfully.")


try:
    students = []  # empty list that will hold all records

    add_student(students, 101, "Aarav Sharma", 88.5)
    add_student(students, 102, "Priya Singh", 92.0)
    add_student(students, 103, "Rohan Verma", 35.0)
    add_student(students, 104, "Neha Gupta", 76.5)
    add_student(students, 102, "Duplicate Entry", 50.0)  # rejected: roll exists

    print(f"\nList created with {len(students)} student records.")
    print(students)
except Exception as e:
    print("Error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Student 'Aarav Sharma' added successfully.
# Student 'Priya Singh' added successfully.
# Student 'Rohan Verma' added successfully.
# Student 'Neha Gupta' added successfully.
# Roll number 102 already exists. Record not added.
#
# List created with 4 student records.
# [{'roll_no': 101, 'name': 'Aarav Sharma', 'marks': 88.5}, {'roll_no': 102, 'name': 'Priya Singh', 'marks': 92.0}, {'roll_no': 103, 'name': 'Rohan Verma', 'marks': 35.0}, {'roll_no': 104, 'name': 'Neha Gupta', 'marks': 76.5}]
