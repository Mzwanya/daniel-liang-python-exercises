'''
(Split digits) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order.
'''

integer_number = eval(input("Enter an integer: "))

first_digit = integer_number % 10 //1
second_digit = integer_number % 100 //10
third_digit = integer_number % 1000 // 100
fourth_digit = integer_number % 10000 // 1000

print(fourth_digit)
print(third_digit)
print(second_digit)
print(first_digit)