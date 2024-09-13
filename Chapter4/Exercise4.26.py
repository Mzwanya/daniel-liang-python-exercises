# Prompt the user to enter a three-digit integer
number = int(input("Enter a three-digit integer: "))

# Get the hundreds and ones digits
hundreds = number // 100
ones = number % 10

# Check if the number is a palindrome
if hundreds == ones:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
