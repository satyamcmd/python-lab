# Q8: Find pairs of numbers in a list whose sum equals a given number
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
target = int(input("Enter the target sum: "))
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):   # j > i so each pair is checked once
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
if len(pairs) == 0:
    print(f"No pairs found with sum {target}.")
else:
    print(f"Pairs with sum {target}:")
    for first, second in pairs:
        print(f"  ({first}, {second})")
