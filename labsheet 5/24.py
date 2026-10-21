first = tuple(input("Enter the first tuple elements separated by spaces: ").split())
second = tuple(input("Enter the second tuple elements separated by spaces: ").split())
common_values = []

for value in first:
    if value in second and value not in common_values:
        common_values.append(value)

print("Common elements:", tuple(common_values))
