"""
Program 10: CRUD operations on a file - add, view, modify and delete records.

Records are stored in records.txt, one per line: roll_no,name,marks
Every action loads the file, changes the data in memory and saves it again.
"""
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records.txt")


def load_records():
    """Read the file and return a list of [roll_no, name, marks] lists."""
    records = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    roll_no, name, marks = line.strip().split(",")
                    records.append([roll_no, name, marks])
    except FileNotFoundError:
        pass  # no file yet = no records
    return records


def save_records(records):
    """Write all records back to the file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for roll_no, name, marks in records:
            file.write(f"{roll_no},{name},{marks}\n")


def add_record():
    """Create: append a new record."""
    records = load_records()
    roll_no = input("Roll No: ").strip()
    if any(r[0] == roll_no for r in records):
        print("This roll number already exists.")
        return
    name = input("Name   : ").strip().replace(",", " ")  # commas would break the format
    try:
        marks = float(input("Marks  : "))
    except ValueError:
        print("Marks must be a number. Record not added.")
        return
    records.append([roll_no, name, str(marks)])
    save_records(records)
    print("Record added successfully.")


def view_records():
    """Read: display all records."""
    records = load_records()
    if not records:
        print("No records found.")
        return
    print(f"\n{'Roll No':<10}{'Name':<20}{'Marks':<8}")
    print("-" * 38)
    for roll_no, name, marks in records:
        print(f"{roll_no:<10}{name:<20}{marks:<8}")


def modify_record():
    """Update: change the name and/or marks of a record."""
    records = load_records()
    roll_no = input("Roll No to modify: ").strip()
    for r in records:
        if r[0] == roll_no:
            name = input(f"New name [{r[1]}]: ").strip().replace(",", " ")
            marks = input(f"New marks [{r[2]}]: ").strip()
            if name:
                r[1] = name
            if marks:
                try:
                    r[2] = str(float(marks))
                except ValueError:
                    print("Invalid marks, old marks kept.")
            save_records(records)
            print("Record modified successfully.")
            return
    print("Record not found.")


def delete_record():
    """Delete: remove a record by roll number."""
    records = load_records()
    roll_no = input("Roll No to delete: ").strip()
    remaining = [r for r in records if r[0] != roll_no]
    if len(remaining) == len(records):
        print("Record not found.")
    else:
        save_records(remaining)
        print("Record deleted successfully.")


def main():
    while True:
        print("\n===== FILE CRUD MENU =====")
        print("1. Add record\n2. View records\n3. Modify record\n4. Delete record\n5. Exit")
        try:
            choice = input("Enter your choice (1-5): ").strip()
        except EOFError:
            break
        try:
            if choice == "1":
                add_record()
            elif choice == "2":
                view_records()
            elif choice == "3":
                modify_record()
            elif choice == "4":
                delete_record()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please enter 1 to 5.")
        except (OSError, ValueError) as e:
            print("File error:", e)


if __name__ == "__main__":
    main()


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Sample input typed by the user (one value per line):
#   2 | 1 | 101 | Aarav Sharma | 88.5 | 1 | 102 | Priya Singh | 92 | 2 | 3 | 102 | <Enter> | 95 | 4 | 101 | 2 | 5
#
# Output:
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): No records found.
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): Roll No: Name   : Marks  : Record added successfully.
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): Roll No: Name   : Marks  : Record added successfully.
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5):
# Roll No   Name                Marks
# --------------------------------------
# 101       Aarav Sharma        88.5
# 102       Priya Singh         92.0
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): Roll No to modify: New name [Priya Singh]: New marks [92.0]: Record modified successfully.
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): Roll No to delete: Record deleted successfully.
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5):
# Roll No   Name                Marks
# --------------------------------------
# 102       Priya Singh         95.0
#
# ===== FILE CRUD MENU =====
# 1. Add record
# 2. View records
# 3. Modify record
# 4. Delete record
# 5. Exit
# Enter your choice (1-5): Goodbye!
