# Q11: Check if two strings are anagrams (ignores case and spaces)
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letter_counts(text):
    # build a dictionary of character -> count (case-insensitive)
    counts = {}
    for ch in text:
        if ch == " ":
            continue
        for i in range(26):          # convert uppercase to lowercase
            if ch == UPPER[i]:
                ch = LOWER[i]
                break
        counts[ch] = counts.get(ch, 0) + 1
    return counts


first = input("Enter first string: ")
second = input("Enter second string: ")
if letter_counts(first) == letter_counts(second):
    print(f'"{first}" and "{second}" are Anagrams.')
else:
    print(f'"{first}" and "{second}" are NOT Anagrams.')
