'''
**5.18 (Find the factors of an integer) Write a program that reads an integer and displays
all its smallest factors, also known as prime factors.
For example, if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
'''
import sys

print("A program that reads a positive integer and displays all its smallest factors (prime factors)")
integer = int(input("Enter an integer: "))
number = 2
quotient = -1
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

'''
# OR
# lines 25 to 30 can be replaced with:
        if quotient != 1:
            print(str(number) + ' *', end=' ')
        elif number == origin:
            print("No other factors, the factor is itself,", number)
        else:
            print(str(number) + ' = ' + str(user_input_original_integer))
    else:
        number+= 1
'''
