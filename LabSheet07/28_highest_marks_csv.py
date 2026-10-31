# 28. Find and display the student record with the highest marks.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    valid_rows = []
    for row in rows:
        try:
            valid_rows.append((float(row["Marks"]), row))
        except (KeyError, ValueError):
            continue

    if valid_rows:
        highest_marks, student = max(valid_rows, key=lambda item: item[0])
        print("Highest marks:", highest_marks)
        print("Student record:", student)
    else:
        print("No valid marks records found.")
except FileNotFoundError:
    print("students.csv was not found.")
