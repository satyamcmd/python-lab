first = set(input("Enter the elements of the first set: ").split())
second = set(input("Enter the elements of the second set: ").split())

if first <= second:
    print("The first set is a subset of the second set.")
else:
    print("The first set is not a subset of the second set.")
