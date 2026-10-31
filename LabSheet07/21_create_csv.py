# 21. Create a CSV file and write student records into it.
import csv

students = [
    ["Name", "Marks", "City"],
    ["Amit", 85, "Delhi"],
    ["Ravi", 92, "Mumbai"],
    ["Priya", 78, "Pune"]
]
try:
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("Data written to students.csv.")
except OSError as error:
    print("File error:", error)
