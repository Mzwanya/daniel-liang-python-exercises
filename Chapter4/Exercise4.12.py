# Check a number

# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

# Check whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just one of them (but not both) and display the result
print(f"Is {number} divisible by 5 and 6?", number % 5 == 0 and number % 6 == 0)
print(f"Is {number} divisible by 5 or 6?", number % 5 == 0 or number % 6 == 0)
print(f"Is {number} divisible by 5 or 6, but not both?", (number % 5 == 0 and number % 6 != 0) or (number % 5 != 0 and number % 6 == 0))
