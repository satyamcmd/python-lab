first = tuple(input("Enter the first tuple elements separated by spaces: ").split())
second = tuple(input("Enter the second tuple elements separated by spaces: ").split())

first, second = second, first

print("First tuple after swapping:", first)
print("Second tuple after swapping:", second)
