# Sum the digits in an integer

# Prompt the user to input an integer number between 0 and 1000
integer_number = eval(input("Enter an integer number between 0 and 1000: "))

# Extracting each digit from the integer number
first_digit = integer_number % 10
integer_number //= 10
second_digit = integer_number % 10
integer_number //= 10
third_digit = integer_number % 10


# Compute sum of the digits
sum_of_digits = first_digit + second_digit + third_digit

# Display the results
print("The sum of the digits is: ", sum_of_digits)
