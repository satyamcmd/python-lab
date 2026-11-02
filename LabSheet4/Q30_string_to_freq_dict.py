# Q30: Create a dictionary from a string: characters as keys, frequency as values
text = input("Enter a string: ")
if text == "":
    print("String is empty.")
else:
    freq_dict = {}
    for ch in text:
        if ch != " ":                      # spaces are skipped
            freq_dict[ch] = freq_dict.get(ch, 0) + 1
    print("Frequency dictionary:", freq_dict)
