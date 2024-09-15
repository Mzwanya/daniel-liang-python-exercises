gck = 1
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
d = min(number1, number2)

while d > 1:
    if number1 % d == 0 and number2 % d == 0:
        print("The gcd is", d)
        break
    d -= 1
    if d == 1:
        print("There is no gcd between " + str(number1) + " and " + str(number2))
