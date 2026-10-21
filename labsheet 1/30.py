print("satyam")

number = int(input("Enter an integer: "))
is_prime = number >= 2

for divisor in range(2, int(number ** 0.5) + 1):
	if number % divisor == 0:
		is_prime = False
		break

if is_prime:
	print("The number is prime.")
else:
	print("The number is not prime.")
