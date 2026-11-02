# Q2: Count vowels and consonants in a string
text = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):  # only alphabets count
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
print(f"Vowels     = {vowels}")
print(f"Consonants = {consonants}")
