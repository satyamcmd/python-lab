"""
Program 9: Save student data into a text file and read it back.

File format: one student per line -> roll_no,name,marks
"""
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students_data.txt")

students = [
    (101, "Aarav Sharma", 88.5),
    (102, "Priya Singh", 92.0),
    (103, "Rohan Verma", 35.0),
]

try:
    # ---- WRITE: "w" creates the file (or overwrites an old one) ----
    # The 'with' statement closes the file automatically.
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for roll_no, name, marks in students:
            file.write(f"{roll_no},{name},{marks}\n")
    print(f"{len(students)} records saved to {os.path.basename(FILE_NAME)}")

    # ---- READ: "r" opens the file for reading ----
    print("\nReading the data back from the file:")
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<8}")
    print("-" * 38)
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            roll_no, name, marks = line.strip().split(",")  # split the line into fields
            print(f"{roll_no:<10}{name:<20}{marks:<8}")
except FileNotFoundError:
    print("File not found.")
except (ValueError, OSError) as e:
    print("Error while handling file:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# 3 records saved to students_data.txt
#
# Reading the data back from the file:
# Roll No   Name                Marks
# --------------------------------------
# 101       Aarav Sharma        88.5
# 102       Priya Singh         92.0
# 103       Rohan Verma         35.0
