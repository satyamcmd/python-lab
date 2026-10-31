# 25. Append a new student record to an existing CSV file.
import csv
from pathlib import Path

filename = Path("students.csv")
try:
    if not filename.exists():
        with filename.open("w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(["Name", "Marks", "City"])
    with filename.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([input("Name: "), input("Marks: "), input("City: ")])
    print("Record appended.")
except OSError as error:
    print("File error:", error)
