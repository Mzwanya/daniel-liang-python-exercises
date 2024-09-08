# Split digits

# Prompt the user to enter a four digit integer number
integer_number = eval(input("Enter an integer: "))

# Spliting the digits
first_digit = integer_number % 10
integer_number //= 10
second_digit = integer_number % 10
integer_number //= 10
third_digit = integer_number % 10
integer_number //= 10
fourth_digit = integer_number % 10

# Display the number in reverse order
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
