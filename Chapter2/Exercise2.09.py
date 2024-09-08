# Science: wind-chill temperature

# Prompt the user to enter the outside temperature and wind speed
outside_temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour greater than 2 miles per hour: "))

# Compute the wind chill temperature
wind_chill_temperature = 35.74 + 0.6215 * outside_temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * outside_temperature * (wind_speed ** 0.16)

# Display the results
print("The wind chill index is", int(wind_chill_temperature * 100000) / 100000.0)
