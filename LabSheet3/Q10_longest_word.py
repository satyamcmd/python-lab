# Q10: Find the longest word in a string
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
    longest = words[0]
    for word in words:
        if len(word) > len(longest):  # first longest word wins ties
            longest = word
    print(f'Longest word: "{longest}" ({len(longest)} characters)')
