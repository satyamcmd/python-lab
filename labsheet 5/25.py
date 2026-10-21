first = tuple(input("Enter the first tuple elements separated by spaces: ").split())
second = tuple(input("Enter the second tuple elements separated by spaces: ").split())
difference = []

for value in first:
    if value not in second and value not in difference:
        difference.append(value)

print("Elements in the first tuple but not the second:", tuple(difference))
