# Q14: Remove all punctuation from a string
PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in PUNCTUATION:
        result += ch
print("Without punctuation:", result)
