'''
*5.26 (Sum a series) Write a program to sum the following series:
1/3 + 3/5 + 5/7 + 7/9 + 9/11 + 11/13 + ... + 95/97 + 97/99
'''
a = 1  # numerator
b = 3  # denominator
summation = 0
while b <= 99:
    summation += a / b
    a += 2
    b += 2
print(summation)
