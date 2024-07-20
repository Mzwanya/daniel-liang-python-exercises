'''
**4.22 (Geometry: point in a circle?) Write a program that prompts the user to enter a
point (x, y) and checks whether the point is within the circle centered at (0, 0) with
radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle, as
shown in Figure 4.8a.
'''
import math

x, y = eval(input("Emter a point with two cordinates: "))
x2, y2 = 0, 0
distance_from_center_to_the_point = math.sqrt(math.pow(x2 - x, 2)  + math.pow(y2 - y, 2))
if distance_from_center_to_the_point <= 10:
    print(f"Point {x, y} is in the circle.")
else:
    print(f"Point {x, y} is outside the circle.")