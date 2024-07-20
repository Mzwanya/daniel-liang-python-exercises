'''
2.8 (Science: calculate energy) Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules.
'''
amount_of_water_in_kilograms = eval(input("Enter the amount of water in kilograms: "))
initial_temperature = eval(input("Enter the initial temperature: "))
final_temperature = eval(input("Enter  the final temperature: "))

energy_needed = amount_of_water_in_kilograms * (final_temperature - initial_temperature) * 4184

print("The energy needed is: ", energy_needed)
