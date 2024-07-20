'''
**2.21 (Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore, the monthly interest rate is After the first month, the value in the account
becomes
100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
(100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month.
'''
monthly_savings_amount = eval(input("Enter the monthly saving amount: "))
annual_interest_rate = 0.05
monthly_interest_rate = annual_interest_rate / 12

amount_after_one_month = monthly_savings_amount * (1 + monthly_interest_rate)
amount_after_two_months = (amount_after_one_month + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_three_months = (amount_after_two_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_four_months = (amount_after_three_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_five_months = (amount_after_four_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)
amount_after_six_months = (amount_after_five_months + monthly_savings_amount) * ( 1 + monthly_interest_rate)

print("After the sixth month, the account value is", int(round(amount_after_six_months * 100)) / 100)


