# Draw a rectangle

import turtle

# Prompt the user to enter the center coordinates (x, y) of a rectangle, width, and height
height = eval(input("Enter the length of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
x, y = eval(input("Enter the cordinates of the Center of the rectangle (x, y): "))

# Draw the rectangle
turtle.penup()
turtle.goto(x - width * 0.5, y + height * 0.5)
turtle.pendown()

turtle.forward(width)
turtle.right(90)

turtle.forward(height)
turtle.right(90)

turtle.forward(width)
turtle.right(90)

turtle.forward(height)

turtle.hideturtle() # hide the turtle pen
turtle.done() # pause turtle window
