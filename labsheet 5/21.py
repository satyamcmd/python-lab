import ast


nested_tuple = ast.literal_eval(
    input("Enter a nested tuple (example: ((1, 2), (3, 4))): ")
)

print("Nested tuple:", nested_tuple)
if nested_tuple and nested_tuple[0]:
    print("First element of the first inner tuple:", nested_tuple[0][0])
else:
    print("The nested tuple has no element at that position.")
