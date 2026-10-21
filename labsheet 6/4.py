items = set(input("Enter the initial set elements separated by spaces: ").split())
new_elements = input("Enter multiple elements to add, separated by spaces: ").split()

items.update(new_elements)
print("Updated set:", items)
