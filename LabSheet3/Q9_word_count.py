# Q9: Count the number of words in a string
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
print(f"Number of words = {len(words)}")
