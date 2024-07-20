# (Geometry: area of a pentagon)

import math

side_length = eval(input("Enter the side: "))

area = (5 * side_length * side_length) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is", area)