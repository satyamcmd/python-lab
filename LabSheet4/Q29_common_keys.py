# Q29: Find common keys between two dictionaries
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


dict_one = read_dict("dictionary 1", "value")
dict_two = read_dict("dictionary 2", "value")
common = []
for key in dict_one:
    if key in dict_two:
        common.append(key)
if len(common) == 0:
    print("No common keys.")
else:
    print("Common keys:", common)
