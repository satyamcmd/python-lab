# Q21: Find the key with the maximum value in a dictionary
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
if len(data) == 0:
    print("Dictionary is empty.")
else:
    best_key = None
    for key in data:
        if best_key is None or data[key] > data[best_key]:
            best_key = key
    print(f'Key with maximum value: "{best_key}" (value = {data[best_key]})')
