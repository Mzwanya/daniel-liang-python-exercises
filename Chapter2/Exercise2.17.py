'''
*2.17 (Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters
'''
weight_in_pounds = eval(input("Enter weight in pounds: "))
height_in_inches = eval(input("Enter height in inches: "))

weight_in_kilos = weight_in_pounds * 0.45359237
height_in_meters = height_in_inches * 0.0254

body_mass_index = weight_in_kilos / (height_in_meters ** 2)

print("BNI is", int(round(body_mass_index * 10000)) / 10000.0)