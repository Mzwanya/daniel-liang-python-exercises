import math

# Input for the first circle
x1 = float(input("Enter the x-coordinate of the center of the first circle: "))
y1 = float(input("Enter the y-coordinate of the center of the first circle: "))
r1 = float(input("Enter the radius of the first circle: "))

# Input for the second circle
x2 = float(input("Enter the x-coordinate of the center of the second circle: "))
y2 = float(input("Enter the y-coordinate of the center of the second circle: "))
r2 = float(input("Enter the radius of the second circle: "))

# Calculate the distance between the centers of the two circles
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Determine if the second circle is inside the first circle
if distance + r2 <= r1:
    print("The second circle is inside the first circle.")
# Determine if the two circles overlap
elif distance < r1 + r2:
    print("The two circles overlap.")
else:
    print("The two circles do not overlap.")
