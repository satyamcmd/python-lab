first = set(input("Enter the first set elements separated by spaces: ").split())
second = set(input("Enter the second set elements separated by spaces: ").split())

print("Union:", first | second)
print("Intersection:", first & second)
print("Difference (first minus second):", first - second)
print("Symmetric difference:", first ^ second)
