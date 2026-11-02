# Q8: Convert a string to title case without built-in functions
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
result = ""
new_word = True  # True when next letter starts a word
for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        result += to_upper(ch)  # first letter uppercase
        new_word = False
    else:
        result += to_lower(ch)  # rest lowercase
print("Title case:", result)
