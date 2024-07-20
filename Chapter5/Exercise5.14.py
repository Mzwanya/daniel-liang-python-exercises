'''
5.14 (Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest
integer n such that n^2 is greater than 12,000.
'''
number = 0
while number * number < 12_000:
    number += 1
    if number * number > 12_000:
        print("The integer is", number)