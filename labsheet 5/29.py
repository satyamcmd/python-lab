values = tuple(input("Enter tuple elements separated by spaces: ").split())

if not values:
    print("The tuple is empty.")
elif all(value == values[0] for value in values):
    print("All elements are the same.")
else:
    print("The elements are not all the same.")
