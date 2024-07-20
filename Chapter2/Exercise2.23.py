# (Turtle: draw four circles) Write a program that prompts the user to enter the radius and draws four circles in the center of the screen

import turtle

radius = eval(input("Enter the radius of the circle: "))

# Drawing Circle 1
turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius)

# Drawing Circle 2
turtle.right(180)
turtle.circle(radius)

# Drawing Circle 3
turtle.left(180)
turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius)

# Drawing Circle 4
turtle.right(180)
turtle.circle(radius)

turtle.done()