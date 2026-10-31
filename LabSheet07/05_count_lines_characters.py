# 5. Count lines and characters in a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("Number of lines:", len(content.splitlines()))
    print("Number of characters:", len(content))
except FileNotFoundError:
    print("sample.txt was not found.")
