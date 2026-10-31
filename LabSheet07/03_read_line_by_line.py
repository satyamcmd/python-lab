# 3. Read a text file one line at a time.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("sample.txt was not found.")
