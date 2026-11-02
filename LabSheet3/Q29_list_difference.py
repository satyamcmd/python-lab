# Q29: Find the difference between two lists (A - B and B - A)
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
only_in_one = []
only_in_two = []
for value in list_one:
    if value not in list_two and value not in only_in_one:
        only_in_one.append(value)
for value in list_two:
    if value not in list_one and value not in only_in_two:
        only_in_two.append(value)
print("List1 - List2:", only_in_one)
print("List2 - List1:", only_in_two)
