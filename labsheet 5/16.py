values = tuple(input("Enter words separated by spaces: ").split())

print("Alphabetical order:", tuple(sorted(values, key=str.casefold)))
