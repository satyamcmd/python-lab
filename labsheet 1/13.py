print("vinit sharma")

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest (in percentage): "))
T = float(input("Enter the time (in years): "))
N = int(input("Enter the number of times interest is compounded per year: "))

A = P * (1 + R / (100 * N)) ** (N * T)
CI = A - P

print("Compound Interest:", CI)
print("Total Amount:", A)
