# Geometry: point in a rectangle?

# Prompt the user to enter the coordinates of the point
x, y = eval(input("Enter a point with two coordinates (x, y): "))

# Rectangle's half-width and alf-height
half_width = 10 / 2
half_height = 5 / 2

# Check if the point is inside the rectangle
if -half_width <= x <= half_width and -half_height <= y <= half_height:
    print(f"The point ({x}, {y}) is inside the rectangle.")
else:
    print(f"The point ({x}, {y}) is outside the rectangle.")
