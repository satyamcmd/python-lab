# 2. Read and display the entire content of a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("sample.txt was not found. Run program 01 first.")
