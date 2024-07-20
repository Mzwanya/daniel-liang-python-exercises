'''
(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32
'''
celsius_reading = eval(input("Enter a degree in Celsius: "))

fahrenheit_reading = (9 / 5) * celsius_reading + 32

print(celsius_reading, "Celsius is", fahrenheit_reading, "Fahrenheit")
