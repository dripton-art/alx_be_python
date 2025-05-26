monthly income = float(input("Enter your monthly income"))
monthly expenses = float(input("Enter your total monthly expenses"))

Monthly Savings = monthly income - monthly expenses

Annual Savings = Monthly Savings * 12

# Assume a simple annual interest rate of 5%
Projected Savings =  Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)

print(f"Monthly Savings are: $[Monthly Savings:.2f]")
print(f"Projected savings after one year, with interest, is: $[Projected Savings:.2f]")
