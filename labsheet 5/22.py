import ast


nested_tuple = ast.literal_eval(
    input("Enter a nested tuple (example: (1, (2, 3), ((4,),))): ")
)
flattened_values = []


def flatten(values):
    for value in values:
        if isinstance(value, tuple):
            flatten(value)
        else:
            flattened_values.append(value)


flatten(nested_tuple)
print("Flattened tuple:", tuple(flattened_values))
