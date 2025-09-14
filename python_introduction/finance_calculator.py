#A program to compute users monthly savings
#Prompt the user for their monthy income and total monthly expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Forecast annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected savings after one year with interest are: {projected_savings}")
