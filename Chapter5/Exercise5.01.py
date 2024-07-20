'''
*5.1 (Count positive and negative numbers and compute the average of numbers)
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the total
and average of the input values (not counting zeros). Your program ends with the
input 0. Display the average as a floating-point number.
'''
number_of_negative_numbers = 0
number_of_positive_numbers = 0
total = 0
integer = -1
while integer != 0:
    integer = int(input("Enter an integer, the input ends if you enter 0: "))
    if integer < 0:
        number_of_positive_numbers += 1
    if integer > 0:
        number_of_negative_numbers += 1
    total += integer

if number_of_positive_numbers == 0 and number_of_negative_numbers == 0:
    print("You didn't enter an any number")
else:
    average = total / (number_of_negative_numbers + number_of_positive_numbers)
    print("The number of positives is", number_of_positive_numbers, '\n' + \
          "The number of negatives is", number_of_negative_numbers, '\n' + \
          "The total is", total, '\n' + \
          "The average is", average)
    