# 6. Display only even-numbered lines (2, 4, 6, ...) from a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number % 2 == 0:
                print(line, end="")
except FileNotFoundError:
    print("sample.txt was not found.")
