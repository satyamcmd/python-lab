# 19. Sort all words alphabetically and save them to a new file.
import re

try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    words = re.findall(r"\\b[\\w']+\\b", content)
    words.sort(key=str.casefold)
    with open("sorted_words.txt", "w", encoding="utf-8") as file:
        file.write("\\n".join(words))
    print("Sorted words saved to sorted_words.txt.")
except FileNotFoundError:
    print("sample.txt was not found.")
