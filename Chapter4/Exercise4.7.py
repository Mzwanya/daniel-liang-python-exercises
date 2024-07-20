'''
4.7 (Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
to display the nonzero denominations only, using singular words for single units
such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
dollars and 3 pennies.
'''
# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of")
# Dollars
if numberOfOneDollars == 1 and numberOfOneDollars != 0:
    print("\t", numberOfOneDollars, "dollar")
elif numberOfOneDollars > 1 and numberOfOneDollars!= 0:
    print("\t", numberOfOneDollars, "dollars")
# Displaying Quarters
if numberOfQuarters == 1 and numberOfQuarters != 0:
    print("\t", numberOfQuarters, "quarter")
elif numberOfQuarters > 1 and numberOfQuarters != 0:
    print("\t", numberOfQuarters, "quarters")

# Displaying Dimes
if numberOfDimes == 1 and numberOfDimes != 0:
    print("\t", numberOfDimes, "dime")
elif numberOfDimes > 1 and numberOfDimes != 0:
    print("\t", numberOfDimes, "dimes")

# Displaying Nickels
if numberOfNickels == 1 and numberOfNickels != 0:
    print("\t", numberOfNickels, "nickel")
elif numberOfNickels > 1 and numberOfNickels != 0:
    print("\t", numberOfNickels, "nickels")
# Displaying Pennies
if numberOfPennies == 1 and numberOfPennies != 0:
    print("\t", numberOfPennies, "penny")
elif numberOfPennies > 1 and numberOfPennies != 0:
    print("\t", numberOfPennies, "pennies")