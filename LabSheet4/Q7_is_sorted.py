# Q7: Check if a list is sorted or not
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
ascending = True
descending = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        ascending = False        # a drop breaks ascending order
    if numbers[i] < numbers[i + 1]:
        descending = False       # a rise breaks descending order
print("List:", numbers)
if ascending:
    print("The list is sorted in ascending order.")
elif descending:
    print("The list is sorted in descending order.")
else:
    print("The list is NOT sorted.")
