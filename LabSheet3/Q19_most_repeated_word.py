# Q19: Find the most repeated word in a string (case-insensitive)
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


def get_words(text):
    # split text into words manually (no split())
    words = []
    current = ""
    for ch in text:
        if ch == " ":
            if current != "":
                words.append(current)
                current = ""
        else:
            current += ch
    if current != "":
        words.append(current)
    return words


text = input("Enter a string: ")
words = get_words(text)
if len(words) == 0:
    print("No words entered.")
else:
    counts = {}
    for word in words:
        key = ""
        for ch in word:
            key += to_lower(ch)       # normalise case
        counts[key] = counts.get(key, 0) + 1
    best_word = None
    best_count = 0
    for word in counts:
        if counts[word] > best_count:
            best_word = word
            best_count = counts[word]
    print(f'Most repeated word: "{best_word}" ({best_count} times)')
