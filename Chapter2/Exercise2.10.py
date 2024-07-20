'''
*2.10 (Physics: find runway length) Given an airplane’s acceleration a and take-off
speed v, you can compute the minimum runway length needed for an airplane to
take off using the following formula: length = v^2/2a
Write a program that prompts the user to enter v in meters/second (m/s) and the
acceleration a in meters/second squared and displays the minimum runway
length.
'''



speed = eval(input("Enter speed: "))
acceleration = eval(input("Enter acceleration: "))

length = (speed  ** 2) / (2 * acceleration)

print("The minimum runway length for this airplane is", int(round(length * 1000)) / 1000.0, "meters")