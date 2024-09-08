# Turtle: draw a cross

import turtle

turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.goto(0, -200)

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200,0)

turtle.done()
