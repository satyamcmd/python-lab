# Q18: Sort the characters of a string alphabetically (bubble sort)
text = input("Enter a string: ")
chars = []
for ch in text:
    chars.append(ch)
n = len(chars)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if chars[j] > chars[j + 1]:   # swap out-of-order neighbours
            chars[j], chars[j + 1] = chars[j + 1], chars[j]
sorted_text = ""
for ch in chars:
    sorted_text += ch
print("Sorted string:", sorted_text)
