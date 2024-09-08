# Area of a triangle)

# Prompt the user to enter the coordinates of three points for a triangle
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

# Calculate the length of each side of the triangle
side1 =  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 =  ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 =  ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

# Compute s
s = (side1 + side2 + side3) / 2

# Compute area
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

# Display the results
print("The area of the triangle is", int(area * 100) / 100.0)