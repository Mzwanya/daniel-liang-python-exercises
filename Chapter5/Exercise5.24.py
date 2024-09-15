'''
**5.24 (Financial application: loan amortization schedule) The monthly payment for a
given loan pays the principal and the interest. The monthly interest is computed by
multiplying the monthly interest rate and the balance (the remaining principal).
The principal paid for the month is therefore the monthly payment minus the
monthly interest. Write a program that , and then 
'''
# Prompt the user enter the loan amount, number of years, and interest rate
loan_amount = eval(input("Loan amount: "))
number_of_years = eval(input("Number of years: "))
annual_interest_rate = eval(input("Annual Interest Rate: "))

monthly_interest_rate = annual_interest_rate / 1200
monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
total_payment = monthly_payment * number_of_years * 12

print("Monthly Payment:", format(monthly_payment, ".2f"))
print("Total Payment:", format(total_payment, ".2f"))

# Compute and display the amortization schedule for the loan
balance = loan_amount
print("Payment#\t Interest\t\t Principal\t\t\t Balance")
for i in range(1, number_of_years * 12 + 1):
    interest = monthly_interest_rate * balance
    principal = monthly_payment - interest
    balance = balance - principal
    print(i, "\t\t", format(interest, ".2f"), "\t\t\t", format(principal, ".2f"), "\t\t\t",
          format(balance, ".2f"))
