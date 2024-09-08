# Science: calculate energy

# Prompt the user to enter amount of water in kilograms and, initial and final temperatures
amount_of_water_in_kilograms = eval(input("Enter the amount of water in kilograms: "))
initial_temperature = eval(input("Enter the initial temperature: "))
final_temperature = eval(input("Enter  the final temperature: "))

# Calculate the energy needed
energy_needed = amount_of_water_in_kilograms * (final_temperature - initial_temperature) * 4184

# Display the results
print("The energy needed is: ", energy_needed)
