items = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to remove: ")

try:
    items.remove(element)
    print("Updated set:", items)
except KeyError:
    print("The element is not in the set.")
