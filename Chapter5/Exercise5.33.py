# Prompt the user for the initial amount, annual percentage yield, and number of months
initial_amount = eval(input("Enter the initial deposit amount: "))
annual_percentage_yield = eval(input("Enter the annual percentage yield: "))
number_of_months = int(input("Enter maturity period (number of months): "))

# Convert annual percentage yield to a monthly interest rate
monthly_interest_rate = annual_percentage_yield / 1200

# Initialize the CD value
cd_value = initial_amount

# Print the table header
print(f"\n{'Month':<10}{'CD Value':<15}")
print("-" * 25)

# Calculate and display the CD value for each month
for month in range(1, number_of_months + 1):
    # Calculate the CD value for the current month
    cd_value += cd_value * monthly_interest_rate
    # Print the month and the CD value
    print(f"{month:<10}{cd_value:,.2f}")
