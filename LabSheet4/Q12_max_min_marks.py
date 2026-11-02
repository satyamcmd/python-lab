# Q12: Find the maximum and minimum marks from a dictionary
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


marks_dict = read_dict("the marks dictionary", "marks")
if len(marks_dict) == 0:
    print("Dictionary is empty.")
else:
    top_name = low_name = None
    for name in marks_dict:
        if top_name is None or marks_dict[name] > marks_dict[top_name]:
            top_name = name
        if low_name is None or marks_dict[name] < marks_dict[low_name]:
            low_name = name
    print(f"Maximum marks: {marks_dict[top_name]} ({top_name})")
    print(f"Minimum marks: {marks_dict[low_name]} ({low_name})")
