# 1. Create a text file and write content into it.
try:
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Hello! This is my first file handling program in Python.\\n")
    print("Content written successfully.")
except OSError as error:
    print("File error:", error)
