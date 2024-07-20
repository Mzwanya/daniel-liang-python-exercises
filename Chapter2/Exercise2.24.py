# (Turtle: draw four hexagons) Write a program that draws four hexagons in the center of the screen
import turtle

# first part
turtle.right(90)
for i in range(6):
    turtle.right(60)
    turtle.forward(100)
turtle.right(60)
turtle.forward(200)

for i in range(5):
    turtle.left(60)
    turtle.forward(100)

# Second part
turtle.right(60)
turtle.penup()
turtle.goto(20, -100)
turtle.pendown()
for i in range(6):
    turtle.right(60)
    turtle.forward(100)
turtle.right(60)
turtle.forward(200)

for i in range(5):
    turtle.left(60)
    turtle.forward(100)

turtle.done()
