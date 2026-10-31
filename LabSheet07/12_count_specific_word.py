# 12. Count occurrences of a specific word (case-insensitive).
word = input("Enter the word to count: ").casefold()
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().casefold().split()
    count = sum(1 for item in words if item.strip(".,!?;:\"'()[]{}") == word)
    print("Occurrences:", count)
except FileNotFoundError:
    print("sample.txt was not found.")
