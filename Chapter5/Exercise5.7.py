'''
5.7 (Use trigonometric functions) Print the following table to display the sin value
and cos value of degrees from 0 to 360 with increments of 10 degrees. Round the
value to keep four digits after the decimal point.
'''
import math

degree = 0
print("Degree       Sin          Cos")
while degree <= 360:
    cos = math.cos(math.radians(degree))
    sin = math.sin(math.radians(degree))
    print(format(degree, "2.0f"), format(sin, '14.4f'), format(cos, '14.4f'))
    degree += 10

