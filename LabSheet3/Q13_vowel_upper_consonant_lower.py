# Q13: Vowels -> uppercase, consonants -> lowercase
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
for ch in text:
    if ch in "aeiouAEIOU":
        result += to_upper(ch)
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        result += to_lower(ch)   # consonant
    else:
        result += ch             # leave spaces/digits/symbols unchanged
print("Result:", result)
