# Q1: Find the sum and average of elements in a list
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
    print("List is empty - cannot compute average.")
else:
    total = 0
    for value in numbers:
        total += value
    average = total / len(numbers)
    print("List:", numbers)
    print(f"Sum     = {total}")
    print(f"Average = {average:.2f}")
