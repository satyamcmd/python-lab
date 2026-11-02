# Q26: Merge two lists into one
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


list_one = read_list("list 1")
list_two = read_list("list 2")
merged = []
for value in list_one:
    merged.append(value)
for value in list_two:
    merged.append(value)
print("Merged list:", merged)
