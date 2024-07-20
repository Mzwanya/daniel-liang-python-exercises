'''
(Convert pounds into kilograms) Write a program that converts pounds into
kilograms. The program prompts the user to enter a value in pounds, converts it to
kilograms, and displays the result. One pound is 0.454 kilograms.
'''
pounds = eval(input("Enter a value in pounds :"))

kilos = pounds * 0.454

print(pounds, "pounds is", int(kilos * 1000) / 1000.0, "kilograms")
