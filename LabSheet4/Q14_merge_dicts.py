# Q14: Merge two dictionaries into one (second overrides on common keys)
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
merged = {}
for key in dict_one:
    merged[key] = dict_one[key]
for key in dict_two:
    merged[key] = dict_two[key]     # common keys take the value from dict 2
print("Dictionary 1:", dict_one)
print("Dictionary 2:", dict_two)
print("Merged      :", merged)
