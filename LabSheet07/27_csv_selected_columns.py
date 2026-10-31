# 27. Display selected columns (Name and Marks) from a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not {"Name", "Marks"}.issubset(reader.fieldnames):
            print("CSV must contain Name and Marks columns.")
        else:
            for row in reader:
                print("Name:", row["Name"], "| Marks:", row["Marks"])
except FileNotFoundError:
    print("students.csv was not found.")
