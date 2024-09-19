# Define the base salary and the target income
base_salary = 5000
target_income = 30000

# Initialize sales amount and total income
sales = 0
total_income = base_salary

# Use a while loop to calculate the minimum sales needed
while total_income < target_income:
    sales += 0.01  # Increment sales by a small value (0.01)

    # Calculate commission based on sales amount
    if sales <= 5000:
        commission = sales * 0.08
    elif sales <= 10000:
        commission = 5000 * 0.08 + (sales - 5000) * 0.10
    else:
        commission = 5000 * 0.08 + 5000 * 0.10 + (sales - 10000) * 0.12

    # Calculate the total income
    total_income = base_salary + commission

# Print the minimum sales amount required to reach the target income
print(f"The minimum sales required to make $30,000 is: ${sales:.2f}")
