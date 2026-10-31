# 29. Search for a student by name in a CSV file (case-insensitive).
import csv

search_name = input("Enter student name: ").strip().casefold()
try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        matches = [
            row for row in csv.DictReader(file)
            if row.get("Name", "").strip().casefold() == search_name
        ]
    if matches:
        for record in matches:
            print(record)
    else:
        print("Student not found.")
except FileNotFoundError:
    print("students.csv was not found.")
