print("satyam")

character = input("Enter a character: ")

if len(character) == 1 and character.isalpha():
	if character.lower() in "aeiou":
		print("The character is a vowel.")
	else:
		print("The character is a consonant.")
else:
	print("Please enter a single alphabetic character.")
