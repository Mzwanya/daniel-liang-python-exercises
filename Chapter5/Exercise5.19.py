# **5.19 (Display a pyramid) Write a program that prompts the user to enter an integer
# from 1 to 15 and displays a pyramid, as shown in the following sample run:

import sys

# TO BE REVISED & IMPROVED LATER

number = int(input("Enter an integer (1 to 15): "))
count = 1
spaces = number * 3
if 1 <= number <= 15:
    for i in range(number + 1):
        print(' ' * spaces, end='')
        for k in range(1, count - 1):
            print(-k + i + 1, end=' ')

        for j in range(1, count):
            print(j, end=' ')
        count += 1
        if i <= 9:
            spaces -= 2
        else:
            spaces -= 3
        print()
else:
    sys.exit("Error: Invalid input")
