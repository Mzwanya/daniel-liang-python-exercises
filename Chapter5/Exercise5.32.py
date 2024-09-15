# Prompt the user for the deposit amount, annual interest rate, and number of months
monthly_deposit = eval(input("Enter the monthly deposit amount: "))
annual_interest_rate = eval(input("Enter the annual interest rate (in percentage): "))
number_of_months = int(input("Enter the number of months: "))

# Convert annual interest rate to a monthly rate
monthly_interest_rate = annual_interest_rate / 1200

# Initialize the account value
account_value = 0.0

# Calculate the value in the account after each month
for month in range(number_of_months):
    # Add the monthly deposit
    account_value += monthly_deposit
    # Apply the monthly interest rate
    account_value *= (1 + monthly_interest_rate)

# Display the final account value
print(f"The amount in the savings account after {number_of_months} months is: ${account_value:.2f}")
