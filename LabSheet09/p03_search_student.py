"""
Program 3: Search for a student by name in the list.

The search ignores upper/lower case and also finds partial names
(searching "singh" finds "Priya Singh").
"""

students = [
    {"roll_no": 101, "name": "Aarav Sharma", "marks": 88.5},
    {"roll_no": 102, "name": "Priya Singh", "marks": 92.0},
    {"roll_no": 103, "name": "Rohan Verma", "marks": 35.0},
    {"roll_no": 104, "name": "Neha Gupta", "marks": 76.5},
]


def search_by_name(students, search_name):
    """Return a list of students whose name contains search_name."""
    search_name = search_name.strip().lower()
    return [s for s in students if search_name in s["name"].lower()]


try:
    # Try one name that exists and one that does not
    for name in ("priya", "Rahul"):
        print(f"Searching for '{name}'...")
        found = search_by_name(students, name)
        if found:
            for s in found:
                print(f"  Found -> Roll No: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")
        else:
            print("  No student found with that name.")
except (KeyError, AttributeError) as e:
    print("Error while searching:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# Searching for 'priya'...
#   Found -> Roll No: 102, Name: Priya Singh, Marks: 92.0
# Searching for 'Rahul'...
#   No student found with that name.
