items = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to check: ")

if element in items:
    print("The element exists in the set.")
else:
    print("The element does not exist in the set.")
