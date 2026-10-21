words = tuple(input("Enter words separated by spaces: ").split())

if words:
    longest_length = max(len(word) for word in words)
    print("Length of the longest word:", longest_length)
else:
    print("The tuple is empty.")
