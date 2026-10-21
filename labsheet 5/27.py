import ast


tuple_list = ast.literal_eval(
    input("Enter a list of tuples (example: [(1, 'a'), (2, 'b')]): ")
)

if tuple_list:
    columns = list(zip(*tuple_list))
    for index, column in enumerate(columns, start=1):
        print("List", index, ":", list(column))
else:
    print("The list of tuples is empty.")
