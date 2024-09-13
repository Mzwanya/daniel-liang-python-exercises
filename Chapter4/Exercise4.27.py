
# Input coordinates for the point
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

# Coordinates of the triangle vertices
x1, y1 = 0, 0
x2, y2 = 200, 0
x3, y3 = 0, 100

# Calculate the area of the original triangle
A = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

# Calculate the areas of the triangles formed with the point
A1 = abs(x *( y2 - y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2.0
A2 = abs(x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y)) / 2.0
A3 = abs(x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) / 2.0

# Check if the point is inside the triangle
if A == A1 + A2 + A3:
    print("The point is inside the triangle.")
else:
    print("The point is outside the triangle.")
