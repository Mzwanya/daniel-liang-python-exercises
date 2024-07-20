'''
5.13 (Find numbers divisible by 5 or 6, but not both) Write a program that displays, ten
numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but
not both. The numbers are separated by exactly one space.
'''

number = 100
count_per_line = 1
limit = 10
print("The integers that are divisible by 5 0r 6 but not both from 100 to 200 are:")
while number <= 200:
    if number % 5 == 0 or number % 6 == 0 and number % 5 != number % 6:
        print(str(number), end=' ')
        if count_per_line % limit == 0:
            print()
        count_per_line += 1

    number += 1
