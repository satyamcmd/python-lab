first = set(input("Enter the first set elements separated by spaces: ").split())
second = set(input("Enter the elements to remove from the first set: ").split())

first.difference_update(second)
print("First set after removal:", first)
