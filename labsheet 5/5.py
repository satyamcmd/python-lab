values = tuple(input("Enter tuple elements separated by spaces: ").split())
start = int(input("Enter the start index: "))
stop = int(input("Enter the stop index: "))

print("Slice:", values[start:stop])
