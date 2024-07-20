# **5.23 (Financial application: compare loans with various interest rates)
# Write a program that lets the user enter the loan amount and
# loan period in years and displays the monthly and total payments
# for each interest rate starting from 5% to 8%, with an increment of 1/8.

loan_amount = eval(input("Loan amount: "))
number_of_years = eval(input("Number of years: "))
print("Interest Rate      Monthly Payment      Total Payment")
annual_interest_rate = 5

while annual_interest_rate <= 8:
    monthly_interest_rate = annual_interest_rate / 1200
    monthly_payment = (loan_amount * monthly_interest_rate /
                       (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12)))
    total_payment = monthly_payment * number_of_years * 12

    print(format(annual_interest_rate, ".3f"), format(monthly_payment, "19.2f"), format(total_payment, "22.2f"))
    annual_interest_rate += 0.125
