# Q16: Sort a dictionary by values (ascending, bubble sort on key list)
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
keys = []
for key in data:
    keys.append(key)
n = len(keys)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if data[keys[j]] > data[keys[j + 1]]:   # compare by value, swap keys
            keys[j], keys[j + 1] = keys[j + 1], keys[j]
sorted_dict = {}
for key in keys:
    sorted_dict[key] = data[key]
print("Original       :", data)
print("Sorted by value:", sorted_dict)
