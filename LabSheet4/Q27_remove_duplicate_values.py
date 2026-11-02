# Q27: Remove duplicate values from a dictionary (first key is kept)
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
seen_values = []
unique = {}
for key in data:
    if data[key] not in seen_values:
        seen_values.append(data[key])
        unique[key] = data[key]
print("Original          :", data)
print("Without duplicates:", unique)
