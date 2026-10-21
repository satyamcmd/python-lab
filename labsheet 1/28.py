print("vinit sharma")

character = input("Enter a character: ")

if len(character) != 1:
	print("Please enter exactly one character.")
elif character.isupper():
	print("The character is uppercase.")
elif character.islower():
	print("The character is lowercase.")
elif character.isdigit():
	print("The character is a digit.")
else:
	print("The character is a special character.")
