# 11. Search for a word in a text file (case-insensitive).
word = input("Enter the word to search: ").casefold()
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    if word and word in content.casefold():
        print("Word found in the file.")
    else:
        print("Word not found.")
except FileNotFoundError:
    print("sample.txt was not found.")
