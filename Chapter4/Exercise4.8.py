'''
*4.8 (Sort three integers) Write a program that prompts the user to enter three integers
and displays them in increasing order.
'''

number1 = int(input("Enter an integer: "))
number2 = int(input("Enter another integer: "))
number3 = int(input("Enter another integer: "))

if number1 >= number2 and number1 >= number3:
    if number2 >= number3:
        print(str(number1) + ',' + str(number2) + ',' + str(number3))
    else:
        print(str(number1) + ',' + str(number3) + ',' + str(number2))
elif number2 >= number1 and number2 >= number3:
    if number1 >= number3:
        print(str(number2) + ',' + str(number1), ',' + str(number3))
    else:
        print(str(number2) + ',' + str(number3) + ',' + str(number1) )
elif number3 >= number1 and number3 >= number2:
    if number1 >= number2:
        print(str(number3) + ',' + str(number1) + ',' + str(number2))
    else:
        print(str(number3) + ',' + str(number2) + ',' + str(number1))
