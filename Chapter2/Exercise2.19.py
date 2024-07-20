# *2.19 (Financial application: calculate future investment value)

investment_amount = eval(input("Enter investment amount: "))
annual_interest_rate = eval(input("Enter annual interest rate: "))
number_of_years = eval(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 1200
number_of_months = number_of_years * 12

future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months

print("Accumulated value is", int(round(future_investment_value * 100)) / 100.0)