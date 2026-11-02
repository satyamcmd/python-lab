# Q15: Find the first non-repeated character in a string
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1  # count occurrences
answer = None
for ch in text:                # scan again in original order
    if frequency[ch] == 1:
        answer = ch
        break
if answer is None:
    print("No non-repeated character found.")
else:
    print(f"First non-repeated character: '{answer}'")
