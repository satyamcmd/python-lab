# Q16: Count digits, alphabets and special characters
text = input("Enter a string: ")
digits = alphabets = special = 0
for ch in text:
    if '0' <= ch <= '9':
        digits += 1
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        alphabets += 1
    else:
        special += 1  # includes spaces and symbols
print(f"Digits             = {digits}")
print(f"Alphabets          = {alphabets}")
print(f"Special characters = {special}")
