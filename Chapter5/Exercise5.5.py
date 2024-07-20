'''
*5.5 (Conversion from kilograms to pounds and pounds to kilograms) Write a program
that displays the following two tables side by side (note that 1 kilogram is 2.2
pounds and that 1 pound is 0.45 kilograms):
'''

count = 0
kilogram1 = 1
pound1 = 0
kilogram2 = 0
pound2 = 20
print("Kilograms        Pounds | Pounds      Kilograms")
while count < 100:
    pound1 = kilogram1 * 2.2
    kilogram2 = pound2  / 2.2
    print(format(kilogram1, "2.0f"), format(pound1, "-18.1f") + '   |  ' + format(pound2, "-2.0f") + format(kilogram2, "18.2f"))
    kilogram1 += 2
    pound2 += 5
    count += 1

