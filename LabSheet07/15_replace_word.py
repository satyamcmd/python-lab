# 15. Replace one word with another throughout a text file.
old_word = input("Word to replace: ")
new_word = input("Replacement word: ")
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    updated = content.replace(old_word, new_word)
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(updated)
    print("Replacement completed.")
except FileNotFoundError:
    print("sample.txt was not found.")
except OSError as error:
    print("File error:", error)
