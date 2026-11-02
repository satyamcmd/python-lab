# Q24: Invert a dictionary (values become keys, keys become values)
# If several keys share a value, their keys are collected in a list.
def read_dict(name, value_label):
    # read n key/value pairs into a dictionary (values are integers)
    n = int(input(f"Enter number of entries in {name}: "))
    if n < 0:
        print("Size cannot be negative.")
        raise SystemExit
    data = {}
    for i in range(n):
        key = input(f"  Enter key {i + 1}: ")
        if key in data:
            print("  Key already exists - value will be overwritten.")
        data[key] = int(input(f"  Enter {value_label} for {key}: "))
    return data


data = read_dict("the dictionary", "value")
inverted = {}
for key in data:
    value = data[key]
    if value not in inverted:
        inverted[value] = key
    elif type(inverted[value]) == list:
        inverted[value].append(key)          # third or later key with same value
    else:
        inverted[value] = [inverted[value], key]   # second key with same value
print("Original:", data)
print("Inverted:", inverted)
