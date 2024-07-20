'''
*2.9 (Science: wind-chill temperature) How cold is it outside? The temperature alone is
not enough to provide the answer. Other factors including wind speed, relative
humidity, and sunshine play important roles in determining coldness outside. In
2001, the National Weather Service (NWS) implemented the new wind-chill temperature to measure the coldness using temperature and wind speed. The formula
is given as follows: t(wc) = 35.74 + 0.6215t(a) - 35.75v^0.16 + 0.4275t(a)v^0.16
where t(a) is the outside temperature measured in degrees Fahrenheit and v is the
speed measured in miles per hour. t(wc) is the wind-chill temperature. The formula
cannot be used for wind speeds below 2 mph or for temperatures below -58F or
above 41°F.
Write a program that prompts the user to enter a temperature between -58F and
41°F and a wind speed greater than or equal to 2 and displays the wind-chill temperature
'''

outside_temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour greater than 2 miles per hour: "))

wind_chill_temperature = 35.74 + 0.6215 * outside_temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * outside_temperature * (wind_speed ** 0.16)

print("The wind chill index is", int(wind_chill_temperature * 100000) / 100000.0)

