# Q24: Reverse a list without built-in functions (two-pointer swap)
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
print("Original:", numbers)
left, right = 0, len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1
print("Reversed:", numbers)
