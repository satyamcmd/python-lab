# Print the sum of first n natural numbers
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)
