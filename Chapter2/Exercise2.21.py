# Financial application: compound value

# Prompt the user to enter the monthly saving amount
monthly_savings_amount = eval(input("Enter the monthly saving amount: "))

# Reading in monthly and annual interest rates
annual_interest_rate = 0.05
monthly_interest_rate = annual_interest_rate / 12

# Calculations
amount_after_one_month = monthly_savings_amount * (1 + monthly_interest_rate)
amount_after_two_months = (amount_after_one_month + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_three_months = (amount_after_two_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_four_months = (amount_after_three_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_five_months = (amount_after_four_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_six_months = (amount_after_five_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)

# Display the account value after the sixth month
print("After the sixth month, the account value is", int(round(amount_after_six_months * 100)) / 100)
