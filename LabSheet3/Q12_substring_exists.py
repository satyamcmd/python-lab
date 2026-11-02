# Q12: Check if a substring exists in a given string
text = input("Enter the main string: ")
sub = input("Enter the substring: ")
if sub == "":
    print("Substring cannot be empty.")
else:
    found_at = -1
    for start in range(len(text) - len(sub) + 1):
        match = True
        for k in range(len(sub)):         # compare character by character
            if text[start + k] != sub[k]:
                match = False
                break
        if match:
            found_at = start
            break
    if found_at != -1:
        print(f'Substring "{sub}" found at index {found_at}.')
    else:
        print(f'Substring "{sub}" NOT found.')
