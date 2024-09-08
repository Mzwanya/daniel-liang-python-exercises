integer_number = int(input("Enter a four digit integer: "))

first_digit = integer_number % 10
integer_number //= 10

second_digit = integer_number % 10
integer_number = integer_number // 10

third_digit = integer_number % 10
integer_number //= 10

fourth_digit = integer_number % 10

print("The reversed number is ", str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit))