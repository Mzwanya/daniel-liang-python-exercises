'''
4.26 (Palindrome number) Write a program that prompts the user to enter a three-digit
integer and determines whether it is a palindrome number. A number is a palindrome
if it reads the same from right to left and from left to right.
'''

number = int(input("Enter a three digit integer: "))

digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10

if str(digit3) + str(digit2) + str(digit1) == str(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")