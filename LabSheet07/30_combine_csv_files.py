# 30. Combine multiple CSV files with the same columns into one CSV file.
import csv

input_files = ["students.csv", "students_extra.csv"]
output_file = "combined_students.csv"

try:
    combined_rows = []
    header = None

    for filename in input_files:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            current_header = next(reader, None)
            if current_header is None:
                continue
            if header is None:
                header = current_header
            elif current_header != header:
                raise ValueError(f"Column headers do not match in {filename}.")
            combined_rows.extend(reader)

    if header is None:
        print("No input CSV data found.")
    else:
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(combined_rows)
        print("Combined data saved to", output_file)
except FileNotFoundError as error:
    print("Required input file not found:", error.filename)
except (OSError, ValueError) as error:
    print("Could not combine files:", error)
