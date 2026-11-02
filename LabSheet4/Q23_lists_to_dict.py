# Q23: Convert two lists into a dictionary (keys list + values list)
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


keys = read_str_list("the keys list")
values = read_str_list("the values list")
if len(keys) != len(values):
    print("Error: both lists must have the same number of items.")
else:
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]   # pair items at the same index
    print("Dictionary:", result)
