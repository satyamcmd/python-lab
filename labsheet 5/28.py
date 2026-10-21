values = tuple(input("Enter tuple elements separated by spaces: ").split())
seen = []
repeated = []

for value in values:
    if value in seen and value not in repeated:
        repeated.append(value)
    elif value not in seen:
        seen.append(value)

print("Repeated items:", tuple(repeated))
