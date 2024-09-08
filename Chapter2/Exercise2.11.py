# Financial application: investment amount)

# Prompt the user to enter the final account value, annual interest rate and the number of years
final_account_value = eval(input("Enter the final account value: "))
annual_interest_rate = eval(input("Enter annual interest rate in percent: "))
number_of_years = eval(input("Enter number of years: "))

# Calculate the monthly interest rate and total number of months
monthly_interest_rate = annual_interest_rate / 1200
number_of_months = number_of_years * 12

# Compute the initial deposit amount
initial_deposit_amount = (final_account_value) / ((1 + monthly_interest_rate) ** number_of_months)

# Display the results
print("Initial deposit value is", initial_deposit_amount)
