integer_number = int(input("Enter a four digit integer: "))

first_digit = integer_number % 10
second = integer_number // 10
second_digit = second % 10

third = integer_number // 100
third_digit = third % 10
fourth = integer_number // 1000
fourth_digit = fourth % 10

print("The reversed number is ", str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit))