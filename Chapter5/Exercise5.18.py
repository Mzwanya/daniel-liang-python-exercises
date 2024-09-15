# A program that reads a positive integer and displays all its smallest factors (prime factors)

import sys

# Prompt the user to enter an integer
integer = int(input("Enter an integer: "))
number = 2

# Check if the input is valid
if integer == 1 or integer == 0:
    print(f"{integer} has no factor")
    sys.exit()
elif integer < 0:
    sys.exit('Error: Invalid input')
else:
    print(f"The factors of {integer} are:", end = ' ')

while integer != 1:
    is_prime = True

    # A loop to find prime numbers from 2, 3, 5...
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    # Test if the prime is a factor of the integer
    if is_prime and integer % number == 0:
        integer = integer / number
        if integer != 1:
            print(str(number) + ',', end=' ')
        else:
            print(str(number))
    else:
        number += 1
