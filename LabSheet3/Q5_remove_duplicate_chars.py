# Q5: Remove all duplicate characters from a string (keep first occurrence)
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in result:  # add only if not seen before
        result += ch
print("String without duplicates:", result)
