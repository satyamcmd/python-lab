values = tuple(input("Enter tuple elements separated by spaces: ").split())
unique_values = []

for value in values:
    if value not in unique_values:
        unique_values.append(value)

print("Tuple without duplicates:", tuple(unique_values))
