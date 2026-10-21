values = tuple(input("Enter tuple elements separated by spaces: ").split())
index = int(input("Enter the index to access: "))

if -len(values) <= index < len(values):
    print("Element:", values[index])
else:
    print("Index is out of range.")
