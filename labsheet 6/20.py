first = set(input("Enter the first set elements separated by spaces: ").split())
second = set(input("Enter the second set elements separated by spaces: ").split())

cartesian_product = {(left, right) for left in first for right in second}
print("Cartesian product:", cartesian_product)
