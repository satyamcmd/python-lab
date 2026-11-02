# Q25: Count the frequency of each element in a list
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
frequency = {}
for value in numbers:
    frequency[value] = frequency.get(value, 0) + 1
print("Element frequencies:")
for value in frequency:
    print(f"  {value} : {frequency[value]}")
