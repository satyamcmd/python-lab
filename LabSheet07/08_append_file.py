# 8. Append new content to an existing text file.
new_content = input("Enter content to append: ")
try:
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write(new_content + "\\n")
    print("Content appended successfully.")
except OSError as error:
    print("File error:", error)
