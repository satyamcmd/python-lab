# Q21: Find largest and smallest elements in a list
def read_list(name):
    # read n integers one by one (no split() needed) with validation
    n = int(input(f"Enter number of elements in {name}: "))
    items = []
    if n < 0:
        print("Size cannot be negative.")
        raise SystemExit
    for i in range(n):
        items.append(int(input(f"  Enter element {i + 1}: ")))
    return items


numbers = read_list("the list")
if len(numbers) == 0:
    print("List is empty.")
else:
    largest = smallest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    print("List:", numbers)
    print("Largest  =", largest)
    print("Smallest =", smallest)
