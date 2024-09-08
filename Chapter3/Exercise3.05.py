# Finding area of a regular polygon

import math

# Prompt the user to enter the number of sides and side length
number_of_sides = eval(input("Enter the number of sides: "))
side_length = eval(input("Enter the side: "))

# Compute area
area = (number_of_sides * side_length * side_length) / (4 * math.tan(math.pi / number_of_sides))

# Display the area
print("The area of the pentagon is", area)
