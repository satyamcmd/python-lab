# Check if a string contains a particular substring
text = input("Enter a string: ")
sub = input("Enter substring: ")

if sub in text:
    print("Substring found")
else:
    print("Substring not found")
