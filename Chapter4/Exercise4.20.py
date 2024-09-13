# Science: wind-chill temperature

outside_temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour greater than 2 miles per hour: "))

if (outside_temperature >= -58 and outside_temperature <= 41) and (wind_speed >= 2):
    wind_chill_temperature = 35.74 + 0.6215 * outside_temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * outside_temperature * (wind_speed ** 0.16)
    print("The wind chill index is", format(wind_chill_temperature, ".5f"))
else:
    if not (outside_temperature >= -58 and outside_temperature <= 41) and not (wind_speed >= 2):
        print("Both temperature and wind speed input are invalid")
    elif not (outside_temperature >= -58 and outside_temperature <= 41):
        print("Invalid temperature input")
    else:
        print("Invalid wind speed input")