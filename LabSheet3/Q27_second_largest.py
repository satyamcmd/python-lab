# Q27: Find the second largest number in a list (distinct values)
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
largest = None
second = None
for value in numbers:
    if largest is None or value > largest:
        second = largest      # old largest becomes second
        largest = value
    elif value != largest and (second is None or value > second):
        second = value
if second is None:
    print("No second largest (need at least two distinct values).")
else:
    print(f"Largest = {largest}, Second largest = {second}")
