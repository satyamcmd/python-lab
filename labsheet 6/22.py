values = input("Enter list elements separated by spaces: ").split()
seen = set()
duplicates = set()

for value in values:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)

print("Duplicate elements:", duplicates)
