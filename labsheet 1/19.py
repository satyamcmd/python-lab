print("vinit sharma")

loan_amount = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (in percentage): "))
tenure_months = int(input("Enter the loan tenure (in months): "))

monthly_rate = annual_rate / (12 * 100)

if monthly_rate == 0:
	emi = loan_amount / tenure_months
else:
	emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)

print("Monthly EMI:", emi)
