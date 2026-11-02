# Q19: Check if a key exists in a dictionary
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
key = input("Enter the key to search: ")
if key in data:
    print(f'Key "{key}" EXISTS with value {data[key]}.')
else:
    print(f'Key "{key}" does NOT exist.')
