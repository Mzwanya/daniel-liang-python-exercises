import math
import turtle

WIDTH = 100
HEIGHT = 50
x, y = eval(input("Enter Point's x,y : "))

# goto to appropriate drawing position
turtle.penup()
turtle.goto(0 - WIDTH / 2, 0 - HEIGHT / 2)
turtle.pendown()

# Draw rectangle
turtle.forward(WIDTH)
turtle.left(90)
turtle.forward(HEIGHT)
turtle.left(90)
turtle.forward(WIDTH)
turtle.left(90)
turtle.forward(HEIGHT)

# Draw dot
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.dot(6)
turtle.end_fill()

turtle.penup()
turtle.goto(-15, -60)
turtle.pendown()

if (WIDTH / 2 > x > -WIDTH / 2) and (HEIGHT / 2 > y > -HEIGHT / 2):
    turtle.write("The Point is inside rectangle")
else:
    turtle.write("The Point is outside rectangle")

turtle.hideturtle()
turtle.done()
