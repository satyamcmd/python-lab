# Q5: Create a list of squares of numbers from 1 to n
n = int(input("Enter n: "))
if n < 1:
    print("n must be at least 1.")
else:
    squares = []
    for number in range(1, n + 1):
        squares.append(number ** 2)
    print(f"Squares from 1 to {n}:", squares)
