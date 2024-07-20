'''
**4.27 (Geometry: points in triangle?) Suppose a right triangle is placed in a plane as
shown below. The right-angle point is at (0, 0), and the other two points are at
(200, 0), and (0, 100). Write a program that prompts the user to enter a point with
x- and y-coordinates and determines whether the point is inside the triangle.
'''
# TO BE FINISHED LATER...
x, y = eval(input("Enter a point's x- and y-coordinates: "))

if x > 200 or y > 200:
    print("The point is not in the triangle")
