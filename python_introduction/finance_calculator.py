monthly_income = float(input("Enter your monthly_income: "))
monthly_expenses = float(input("Enter your total monthly_expenses: "))
Monthly_Savings = monthly_income - monthly_expenses
annual_savings = Monthly_Savings * 12
Projected_Savings =  annual_savings + (annual_savings * 0.05)

print(f"\nYour Monthly_Savings are ${Monthly_Savings:.2f}.")
print(f"Projected_Savings after one year, with interest, is: ${Projected_Savings:.2f}")
