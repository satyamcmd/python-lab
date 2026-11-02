# Q17: Print all substrings of a string
text = input("Enter a string: ")
if text == "":
    print("String is empty.")
else:
    count = 0
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):  # end is exclusive
            print(text[start:end])
            count += 1
    print(f"Total substrings = {count}")
