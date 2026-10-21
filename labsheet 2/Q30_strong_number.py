# Check if a number is strong
num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    num = num // 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
