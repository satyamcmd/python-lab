items = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to discard: ")

items.discard(element)
print("Updated set:", items)
