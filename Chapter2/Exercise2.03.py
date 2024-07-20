'''
(Convert feet into meters) Write a program that reads a number in feet, converts it
to meters, and displays the result. One foot is 0.305 meters.
'''
feets = eval(input("Enter a value for feet: "))

meters = feets * 0.305

print(feets, "feet is", int(meters * 10000) / 1000.0, "meters.")

