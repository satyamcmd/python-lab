first = set(input("Enter the first set elements separated by spaces: ").split())
second = set(input("Enter the second set elements separated by spaces: ").split())

if first.isdisjoint(second):
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")
