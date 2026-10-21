first = tuple(
    int(value) for value in input("Enter the first tuple of numbers: ").split()
)
second = tuple(
    int(value) for value in input("Enter the second tuple of numbers: ").split()
)

if len(first) != len(second):
    print("The tuples must have the same length.")
else:
    element_wise_sum = tuple(
        first[index] + second[index] for index in range(len(first))
    )
    print("Element-wise sum:", element_wise_sum)
