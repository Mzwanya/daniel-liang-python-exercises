# Draw a circle and display it's area

import turtle

# Prompt the user to enter the center and radius of a circle
x, y = eval(input("Enter the cordinates of the Center of the Circle (x, y): "))
radius = eval(input("Enter the radius of the Circle: "))
PI = 3.14158 # Constant pi

# Compute area of the circle
area = radius * radius * PI

# Draw the circle and display its area at the center
turtle.penup()
turtle.goto(x, y)
turtle.write(area)
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()
