# Q4: Extract all uppercase characters from a string
text = input("Enter a string: ")
uppercase_chars = ""
for ch in text:
    if 'A' <= ch <= 'Z':
        uppercase_chars += ch
if uppercase_chars == "":
    print("No uppercase characters found.")
else:
    print("Uppercase characters:", uppercase_chars)
