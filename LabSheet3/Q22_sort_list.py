# Q22: Sort a list in ascending and descending order (bubble sort)
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
ascending = []
for value in numbers:
    ascending.append(value)  # work on a copy
n = len(ascending)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ascending[j] > ascending[j + 1]:
            ascending[j], ascending[j + 1] = ascending[j + 1], ascending[j]
descending = []
for index in range(n - 1, -1, -1):  # descending = ascending read backwards
    descending.append(ascending[index])
print("Original  :", numbers)
print("Ascending :", ascending)
print("Descending:", descending)
