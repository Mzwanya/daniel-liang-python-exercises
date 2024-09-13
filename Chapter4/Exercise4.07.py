# Financial application: monetary units

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25

# Find the number of dimes in the remaining amount
remainingAmount = remainingAmount % 25
numberOfDimes = remainingAmount // 10

# Find the number of nickels in the remaining amount
remainingAmount = remainingAmount % 10
numberOfNickels = remainingAmount // 5

# Find the number of pennies in the remaining amount
remainingAmount = remainingAmount % 5
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of")
# Dollars
if numberOfOneDollars == 1:
    print("\t", numberOfOneDollars, "dollar")
elif numberOfOneDollars > 1:
    print("\t", numberOfOneDollars, "dollars")
# Displaying Quarters
if numberOfQuarters == 1:
    print("\t", numberOfQuarters, "quarter")
elif numberOfQuarters > 1:
    print("\t", numberOfQuarters, "quarters")

# Displaying Dimes
if numberOfDimes == 1:
    print("\t", numberOfDimes, "dime")
elif numberOfDimes > 1:
    print("\t", numberOfDimes, "dimes")

# Displaying Nickels
if numberOfNickels == 1:
    print("\t", numberOfNickels, "nickel")
elif numberOfNickels > 1:
    print("\t", numberOfNickels, "nickels")
# Displaying Pennies
if numberOfPennies == 1:
    print("\t", numberOfPennies, "penny")
elif numberOfPennies > 1:
    print("\t", numberOfPennies, "pennies")
