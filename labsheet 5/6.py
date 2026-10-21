values = tuple(input("Enter tuple elements separated by spaces: ").split())
element = input("Enter the element to search for: ")

if element in values:
    print("The element exists in the tuple.")
else:
    print("The element does not exist in the tuple.")
