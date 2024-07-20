'''
*2.5 (Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.
'''

subtotal = eval(input("Enter the subtotal: "))
gratuity_rate = eval(input("Enter the gratuity rate: "))

gratuity = subtotal * gratuity_rate / 100
total = subtotal + gratuity

print("The gratuity is", int(gratuity * 100) / 100.0, "and the total is", int(total * 100) / 100.0)