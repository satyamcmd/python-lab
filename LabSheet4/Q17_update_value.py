# Q17: Update the value of a key in a dictionary
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
print("Current dictionary:", data)
key = input("Enter the key to update: ")
if key in data:
    new_value = int(input("Enter the new value: "))
    data[key] = new_value
    print("Updated dictionary:", data)
else:
    print(f'Key "{key}" not found - nothing updated.')
