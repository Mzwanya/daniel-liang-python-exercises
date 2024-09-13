import turtle

# Input coordinates for p0, p1, and p2
x0 = float(input("Enter the x-coordinate for p0: "))
y0 = float(input("Enter the y-coordinate for p0: "))

x1 = float(input("Enter the x-coordinate for p1: "))
y1 = float(input("Enter the y-coordinate for p1: "))

x2 = float(input("Enter the x-coordinate for p2: "))
y2 = float(input("Enter the y-coordinate for p2: "))

# Setup turtle window
turtle.setup(600, 600)
turtle.speed(0)

# Draw the point p0
turtle.penup()
turtle.goto(x0, y0)
turtle.dot(10, "red")
turtle.write(f"p0 ({x0}, {y0})", font=("Arial", 12, "normal"))

# Draw the point p1
turtle.goto(x1, y1)
turtle.dot(10, "blue")
turtle.write(f"p1 ({x1}, {y1})", font=("Arial", 12, "normal"))

# Draw the point p2
turtle.goto(x2, y2)
turtle.dot(10, "green")
turtle.write(f"p2 ({x2}, {y2})", font=("Arial", 12, "normal"))

# Draw the line from p0 to p1
turtle.goto(x0, y0)
turtle.pendown()
turtle.goto(x1, y1)

# Calculate the position of p2 relative to the line from p0 to p1
position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

# Display message depending on the position of p2
turtle.penup()
turtle.goto(-200, 200)

if position > 0:
    turtle.write("p2 is on the left side of the line from p0 to p1.", font=("Arial", 16, "normal"))
elif position < 0:
    turtle.write("p2 is on the right side of the line from p0 to p1.", font=("Arial", 16, "normal"))
else:
    turtle.write("p2 is on the line from p0 to p1.", font=("Arial", 16, "normal"))

# Keep the window open
turtle.hideturtle()
turtle.done()
