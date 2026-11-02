# Q13: Count the frequency of characters in a string using a dictionary
text = input("Enter a string: ")
if text == "":
    print("String is empty.")
else:
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1      # seen before: increment
        else:
            frequency[ch] = 1       # first time: start at 1
    print(f"\n{'Char':<8}{'Count':>6}")
    print("-" * 14)
    for ch in frequency:
        shown = "(space)" if ch == " " else ch
        print(f"{shown:<8}{frequency[ch]:>6}")
