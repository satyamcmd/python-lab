# Q23: Remove duplicate elements from a list
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
unique = []
for value in numbers:
    if value not in unique:  # keep first occurrence only
        unique.append(value)
print("Original:", numbers)
print("Without duplicates:", unique)
