# Q2: Rotate a list by n positions (left rotation; negative n rotates right)
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
size = len(numbers)
if size == 0:
    print("List is empty.")
else:
    positions = int(input("Enter number of positions to rotate left: "))
    shift = positions % size          # rotating by size gives the same list
    rotated = []
    for i in range(size):
        rotated.append(numbers[(i + shift) % size])  # element i moves shift places left
    print("Original:", numbers)
    print(f"Rotated by {positions}:", rotated)
