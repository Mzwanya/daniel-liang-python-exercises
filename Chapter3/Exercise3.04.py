# Finding area of a pentagon

import math

# Prompt the user to enter the side
side_length = eval(input("Enter the side: "))

# Compute area
area = (5 * side_length ** 2) / (4 * math.tan(math.pi / 5))

# Display the area
print("The area of the pentagon is", area)
