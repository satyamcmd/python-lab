# Q22: Create a dictionary with numbers as keys and their squares as values
n = int(input("Enter n: "))
if n < 1:
    print("n must be at least 1.")
else:
    squares = {}
    for number in range(1, n + 1):
        squares[number] = number ** 2
    print(squares)
