from itertools import combinations


items = set(input("Enter set elements separated by spaces: ").split())
power_set = set()
elements = list(items)

for size in range(len(elements) + 1):
    for combination in combinations(elements, size):
        power_set.add(frozenset(combination))

print("Power set:", power_set)
