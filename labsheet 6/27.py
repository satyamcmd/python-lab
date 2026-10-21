first = input("Enter the first string: ").replace(" ", "").lower()
second = input("Enter the second string: ").replace(" ", "").lower()
first_letters = set(first)
second_letters = set(second)

same_letters = first_letters == second_letters
same_counts = same_letters and all(first.count(letter) == second.count(letter) for letter in first_letters)

if same_counts:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
