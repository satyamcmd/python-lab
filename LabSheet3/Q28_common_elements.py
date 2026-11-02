# Q28: Find common elements in two lists
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
common = []
for value in list_one:
    if value in list_two and value not in common:
        common.append(value)
if len(common) == 0:
    print("No common elements.")
else:
    print("Common elements:", common)
