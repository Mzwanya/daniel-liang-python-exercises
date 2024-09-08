# Turtle: display a STOP sign

import turtle

turtle.begin_fill()
turtle.color("red")
turtle.circle(100, steps = 6)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-50, 80)
turtle.color("white")
turtle.write("STOP", font = ("Arial", 30, "normal"))
turtle.end_fill()

turtle.hideturtle()
turtle.done()
