# Q25: Count word frequency in a paragraph using a dictionary (case-insensitive)
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_lower(ch):
    # manual lowercase conversion (no .lower())
    for i in range(26):
        if UPPER[i] == ch:
            return LOWER[i]
    return ch


PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
paragraph = input("Enter a paragraph: ")
# clean: lowercase, punctuation replaced by nothing
cleaned = ""
for ch in paragraph:
    if ch not in PUNCTUATION:
        cleaned += to_lower(ch)
# manual word split
words = []
current = ""
for ch in cleaned + " ":
    if ch == " ":
        if current != "":
            words.append(current)
            current = ""
    else:
        current += ch
if len(words) == 0:
    print("No words found.")
else:
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    print(f"\n{'Word':<15}{'Count':>6}")
    print("-" * 21)
    for word in frequency:
        print(f"{word:<15}{frequency[word]:>6}")
