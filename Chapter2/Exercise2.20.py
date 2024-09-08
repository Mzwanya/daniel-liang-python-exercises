# Financial application: calculate interest

# Prompt the user to enter balance and interest rate
balance, annual_interest_rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

# Compute interest
interest = balance * (annual_interest_rate / 1200)

# Display the results
print("The interest is", int(round(interest * 100000)) / 100000.0)
