# Sort three integers

# Prompt the user to enter three integers
number1 = int(input("Enter an integer: "))
number2 = int(input("Enter another integer: "))
number3 = int(input("Enter another integer: "))

# Display the integers in increasing order
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
