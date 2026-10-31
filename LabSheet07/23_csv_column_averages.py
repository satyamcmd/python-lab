# 23. Calculate averages for numeric columns in a CSV file with headers.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("The CSV file has no data rows.")
    else:
        for column in reader.fieldnames:
            numeric_values = []
            for row in rows:
                try:
                    numeric_values.append(float(row[column]))
                except (ValueError, TypeError):
                    pass
            if numeric_values:
                print(f"Average of {column}: {sum(numeric_values) / len(numeric_values):.2f}")
except FileNotFoundError:
    print("students.csv was not found.")
