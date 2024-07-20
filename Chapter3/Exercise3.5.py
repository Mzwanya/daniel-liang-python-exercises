# *3.5 (Geometry: area of a regular polygon)

import math

number_of_sides = eval(input("Enter the number of sides: "))
side_length = eval(input("Enter the side: "))

area = (number_of_sides * side_length * side_length) / (4 * math.tan(math.pi / number_of_sides))
print("The area of the pentagon is", area)