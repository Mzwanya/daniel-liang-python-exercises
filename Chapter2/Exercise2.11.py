'''
*2.11 (Financial application: investment amount)
'''
final_account_value = eval(input("Enter the final account value: "))
annual_interest_rate = eval(input("Enter annual interest rate in percent: "))
number_of_years = eval(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 1200
number_of_months = number_of_years * 12
initial_deposit_amount = (final_account_value) / ((1 + monthly_interest_rate) ** number_of_months)

print("Initial deposit value is", initial_deposit_amount)
