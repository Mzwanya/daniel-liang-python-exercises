'''
**2.6 (Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
10 = 93.)
'''
integer_number = eval(input("Enter an integer number between 0 and 1000: "))

first_digit = integer_number % 10 //1
second_digit = integer_number % 100 //10
third_digit = integer_number % 1000 // 100
fourth_digit = integer_number % 10000 // 1000

sum_of_digits = first_digit + second_digit + third_digit + fourth_digit

print("The sum of the digits is: ", sum_of_digits)

