'''
5.15 (Find the largest n such that n^3 < 12,000) Use a while loop to find the largest
integer n such that n^3 is less than 12,000.
'''
number = 0
while number * number * number < 12_000:
    number += 1
    if number * number * number > 12_000:
        print("The integer is", number - 1)