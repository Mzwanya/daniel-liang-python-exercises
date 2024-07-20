'''
**4.4 (Game: learn addition) Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise. The program is similar to Listing 4.1.
'''
import random

# Generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

# Display result
print(number1, "+", number2, "=", answer, "is", answer == number1 + number2)
