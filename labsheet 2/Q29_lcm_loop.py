# Find the LCM of two numbers using a loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + 1

print("LCM =", lcm)
