values = tuple(input("Enter tuple elements separated by spaces: ").split())
element = input("Enter the element to find: ")

if element in values:
    print("Index:", values.index(element))
else:
    print("The element is not in the tuple.")
