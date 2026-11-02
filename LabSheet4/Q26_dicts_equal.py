# Q26: Check if two dictionaries are equal
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
equal = True
if len(dict_one) != len(dict_two):
    equal = False                      # different sizes can never be equal
else:
    for key in dict_one:
        if key not in dict_two or dict_one[key] != dict_two[key]:
            equal = False
            break
if equal:
    print("The dictionaries are EQUAL.")
else:
    print("The dictionaries are NOT equal.")
