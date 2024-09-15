import math

degree = 0
print("Degree       Sin          Cos")
while degree <= 360:
    cos = math.cos(math.radians(degree))
    sin = math.sin(math.radians(degree))
    print(format(degree, "2.0f"), format(sin, '14.4f'), format(cos, '14.4f'))
    degree += 10
