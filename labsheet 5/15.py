values = tuple(
    int(value) for value in input("Enter numbers separated by spaces: ").split()
)

print("Ascending order:", tuple(sorted(values)))
