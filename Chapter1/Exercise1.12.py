# Turtle: draw four squares

import turtle

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()

turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(200,200)
turtle.goto(-200,200)

turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.goto(0, -200)

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200,0)


turtle.done()