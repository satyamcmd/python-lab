# Q10: Convert a list into a string without using join()
def read_str_list(name):
    # read n strings one by one with validation
    n = int(input(f"Enter number of items in {name}: "))
    if n < 0:
        print("Size cannot be negative.")
        raise SystemExit
    items = []
    for i in range(n):
        items.append(input(f"  Enter item {i + 1}: "))
    return items


items = read_str_list("the list")
result = ""
for index in range(len(items)):
    result += items[index]
    if index != len(items) - 1:
        result += " "               # separator between items
print("List  :", items)
print(f'String: "{result}"')
