# Q1: Check if a string is a palindrome (ignores case and spaces)
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_lower(ch):
    # return lowercase form of a character (manual lookup, no .lower())
    for i in range(26):
        if UPPER[i] == ch:
            return LOWER[i]
    return ch


def to_upper(ch):
    # return uppercase form of a character (manual lookup, no .upper())
    for i in range(26):
        if LOWER[i] == ch:
            return UPPER[i]
    return ch


text = input("Enter a string: ")
cleaned = ""
for ch in text:
    if ch != " ":
        cleaned += to_lower(ch)  # normalise: lowercase, no spaces
left, right = 0, len(cleaned) - 1
is_palindrome = True
while left < right:               # compare from both ends
    if cleaned[left] != cleaned[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print(f'"{text}" is a Palindrome.')
else:
    print(f'"{text}" is NOT a Palindrome.')
