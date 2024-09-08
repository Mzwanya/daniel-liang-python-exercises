# Turtle: draw four circles

import turtle

# Drawing Circle 1
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.circle(50)

# Drawing Circle 2
turtle.right(180)
turtle.circle(50)

# Drawing Circle 3
turtle.left(180)
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.circle(50)

# Drawing Circle 4
turtle.right(180)
turtle.circle(50)

turtle.done()
