# Q30: Separate even and odd numbers from a list
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
evens = []
odds = []
for value in numbers:
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)
print("Even numbers:", evens)
print("Odd numbers :", odds)
