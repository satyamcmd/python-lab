# 16. Display the first and last lines of a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        print("First line:", lines[0], end="" if lines[0].endswith("\\n") else "\\n")
        print("Last line:", lines[-1], end="" if lines[-1].endswith("\\n") else "\\n")
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("sample.txt was not found.")
