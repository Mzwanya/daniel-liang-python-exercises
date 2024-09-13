# Input for the first rectangle
x1 = float(input("Enter the x-coordinate of the center of the first rectangle: "))
y1 = float(input("Enter the y-coordinate of the center of the first rectangle: "))
w1 = float(input("Enter the width of the first rectangle: "))
h1 = float(input("Enter the height of the first rectangle: "))

# Input for the second rectangle
x2 = float(input("Enter the x-coordinate of the center of the second rectangle: "))
y2 = float(input("Enter the y-coordinate of the center of the second rectangle: "))
w2 = float(input("Enter the width of the second rectangle: "))
h2 = float(input("Enter the height of the second rectangle: "))

# Calculate the edges of the first rectangle
left1 = x1 - w1 / 2
right1 = x1 + w1 / 2
bottom1 = y1 - h1 / 2
top1 = y1 + h1 / 2

# Calculate the edges of the second rectangle
left2 = x2 - w2 / 2
right2 = x2 + w2 / 2
bottom2 = y2 - h2 / 2
top2 = y2 + h2 / 2

# Check if the second rectangle is inside the first rectangle
if (left2 >= left1 and right2 <= right1 and
    bottom2 >= bottom1 and top2 <= top1):
    print("The second rectangle is inside the first rectangle.")
# Check if the two rectangles overlap
elif not (left2 > right1 or right2 < left1 or
          top2 < bottom1 or bottom2 > top1):
    print("The second rectangle overlaps with the first rectangle.")
else:
    print("The second rectangle does not overlap with the first rectangle.")
