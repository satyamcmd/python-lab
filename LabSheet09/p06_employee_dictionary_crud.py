"""
Program 6: CRUD operations on a dictionary of employee data.

The dictionary key is the employee ID; the value is another dictionary
holding the employee's details.
"""

employees = {}  # {emp_id: {"name": ..., "department": ..., "salary": ...}}


def create_employee(emp_id, name, department, salary):
    """Create: add a new employee."""
    if emp_id in employees:
        print(f"Employee ID {emp_id} already exists.")
        return
    employees[emp_id] = {"name": name, "department": department, "salary": salary}
    print(f"Employee {emp_id} ({name}) created.")


def read_employees():
    """Read: display all employees."""
    if not employees:
        print("No employees found.")
        return
    print(f"{'ID':<6}{'Name':<18}{'Department':<14}{'Salary':<10}")
    print("-" * 48)
    for emp_id, info in employees.items():
        print(f"{emp_id:<6}{info['name']:<18}{info['department']:<14}{info['salary']:<10}")


def update_employee(emp_id, **changes):
    """Update: change one or more fields of an employee."""
    if emp_id not in employees:
        print(f"Employee ID {emp_id} not found.")
        return
    employees[emp_id].update(changes)  # dict.update() merges the new values
    print(f"Employee {emp_id} updated: {changes}")


def delete_employee(emp_id):
    """Delete: remove an employee by ID."""
    if employees.pop(emp_id, None) is None:  # pop returns None if key is missing
        print(f"Employee ID {emp_id} not found.")
    else:
        print(f"Employee {emp_id} deleted.")


try:
    print("--- CREATE ---")
    create_employee(1, "Ankit Rawat", "IT", 55000)
    create_employee(2, "Sunita Devi", "HR", 48000)
    create_employee(3, "Manoj Kumar", "Finance", 60000)

    print("\n--- READ ---")
    read_employees()

    print("\n--- UPDATE ---")
    update_employee(2, salary=52000, department="Admin")
    update_employee(9, salary=1)  # missing ID

    print("\n--- DELETE ---")
    delete_employee(3)
    delete_employee(3)  # already deleted

    print("\n--- FINAL DATA ---")
    read_employees()
except Exception as e:
    print("Error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# --- CREATE ---
# Employee 1 (Ankit Rawat) created.
# Employee 2 (Sunita Devi) created.
# Employee 3 (Manoj Kumar) created.
#
# --- READ ---
# ID    Name              Department    Salary
# ------------------------------------------------
# 1     Ankit Rawat       IT            55000
# 2     Sunita Devi       HR            48000
# 3     Manoj Kumar       Finance       60000
#
# --- UPDATE ---
# Employee 2 updated: {'salary': 52000, 'department': 'Admin'}
# Employee ID 9 not found.
#
# --- DELETE ---
# Employee 3 deleted.
# Employee ID 3 not found.
#
# --- FINAL DATA ---
# ID    Name              Department    Salary
# ------------------------------------------------
# 1     Ankit Rawat       IT            55000
# 2     Sunita Devi       Admin         52000
