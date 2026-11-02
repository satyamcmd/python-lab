# Q9: Flatten a nested list
def build_list(level):
    # build a (possibly nested) list from user input, recursively
    indent = "  " * level
    count = int(input(f"{indent}Number of items in this list: "))
    items = []
    for i in range(count):
        entry = input(f"{indent}Item {i + 1} - enter an integer, or L for a sub-list: ")
        if entry == "L" or entry == "l":
            items.append(build_list(level + 1))   # nested list
        else:
            items.append(int(entry))
    return items


def flatten(items, result):
    # visit every element; recurse into sub-lists
    for item in items:
        if type(item) == list:
            flatten(item, result)
        else:
            result.append(item)


nested = build_list(0)
flat = []
flatten(nested, flat)
print("Nested list:", nested)
print("Flattened  :", flat)
