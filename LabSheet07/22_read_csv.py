# 22. Read and display all rows from a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            print(row)
except FileNotFoundError:
    print("students.csv was not found. Run program 21 first.")
