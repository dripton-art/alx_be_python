monthly income = float(input("Enter your monthly income: "))
monthly expenses = float(input("Enter your total monthly expenses: "))
Monthly Savings = monthly income - monthly expenses
Projected Savings =  Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)

print(f"\nYour Monthly Savings are $[Monthly Savings:.2f].")
print(f"Projected Savings after one year, with interest, is: $[Projected Savings:.2f]")
