# Q7: Reverse a string without using slicing
text = input("Enter a string: ")
reversed_text = ""
for index in range(len(text) - 1, -1, -1):  # walk from last index to first
    reversed_text += text[index]
print("Reversed string:", reversed_text)
