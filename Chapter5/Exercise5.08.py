'''
5.8 (Use the math.sqrt function) Write a program that prints the following table
using the sqrt function in the math module
'''
import math

number = 0
print("Number     Square Root")
while number <= 20:
    print(format(number, "2.0f"), format(math.sqrt(number), "15.4f"))
    number += 2