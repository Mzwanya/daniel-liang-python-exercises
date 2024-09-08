# Finding the great circle distance

import math

# Prompt the user to input point 1 and 2 in degrees
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

# Convert degrees to radian measure
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)

# Compute distance between the two points
EARTH_RADIUS = 6371.01
distance = EARTH_RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# Display the results
print("The distance between the two points is", distance, "km.")
