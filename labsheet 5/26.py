import ast


tuple_pairs = ast.literal_eval(
    input("Enter a tuple of key-value pairs (example: (('a', 1), ('b', 2))): ")
)
dictionary = dict(tuple_pairs)

print("Dictionary:", dictionary)
