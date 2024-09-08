# Financial application: calculate future investment value

# Prompt the user to enter the investment amount, annual interet rate and number of years
investment_amount = eval(input("Enter investment amount: "))
annual_interest_rate = eval(input("Enter annual interest rate: "))
number_of_years = eval(input("Enter number of years: "))

# Compute the monthly interest rate and number of months
monthly_interest_rate = annual_interest_rate / 1200
number_of_months = number_of_years * 12

# Compute the future investment value
future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months

# Display the results
print("Accumumulated value is", int(round(future_investment_value * 100)) / 100.0)
