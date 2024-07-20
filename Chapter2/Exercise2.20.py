# *2.20 (Financial application: calculate interest)

balance, annual_interest_rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

interest = balance * (annual_interest_rate / 1200)

print("The interest is", int(round(interest * 100000)) / 100000.0)
