'''
*4.25 (Geometry: intersecting point) Two points on line 1 are given as (x1, y1) and (x2,
y2) and on line 2 as (x3, y3) and (x4, y4), as shown in Figure 4.9a–b
'''
# The intersecting point of the two lines can be found by solving the following linear equation:
# (y1 - y2) * x - (x1 - x2) * y = (y1 - y2) * x1 - (x1 - x2) * y1
# (y3 - y4)x - (x3 - x 4)y = (y3 - y4)x3 - (x3 - x 4)y3
# ax + by = e
# cx + dy = f

x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4 : "))
a = y1 - y2
b = x1 - x2
c = y3 - y4
d = x3 - x4
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

if (a * d - b * c) == 0:
    print("The two lines are parallel.")
else:
    x = (e * d - b * f) / (a * d - b * c)        # Cramer's Rule
    y = (a * f - e * c) / (a * d - b * c)        # Cramer's Rule
    print(f"The intersecting point is {x, y}")
