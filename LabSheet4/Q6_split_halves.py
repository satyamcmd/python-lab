# Q6: Split a list into two halves (middle element goes to the second half if odd)
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
middle = len(numbers) // 2
first_half = []
second_half = []
for index in range(len(numbers)):
    if index < middle:
        first_half.append(numbers[index])
    else:
        second_half.append(numbers[index])
print("Original   :", numbers)
print("First half :", first_half)
print("Second half:", second_half)
