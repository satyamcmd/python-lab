# Q4: Find the product of all elements in a list
def read_list(name):
    # read n integers one by one (no split() needed) with validation
    n = int(input(f"Enter number of elements in {name}: "))
    if n < 0:
        print("Size cannot be negative.")
        raise SystemExit
    items = []
    for i in range(n):
        items.append(int(input(f"  Enter element {i + 1}: ")))
    return items


numbers = read_list("the list")
if len(numbers) == 0:
    print("List is empty.")
else:
    product = 1
    for value in numbers:
        product *= value
    print("List:", numbers)
    print("Product =", product)
