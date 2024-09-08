# Area of a pentagon

import math

# Prompt the user to enter the length from the center to a vertex
radius = eval(input("Enter the length from the center to a vertex: "))

# Compute the length of one side
side = 2 * radius * math.sin(math.pi / 5)

# Compute area of the pentagon
area = (3 * math.sqrt(3)) * (side ** 2) / 2

# Display the area
print("The area of the pentagon is", format(area, ".2f"))
