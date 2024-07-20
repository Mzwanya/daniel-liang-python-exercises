'''
*3.13 (Turtle: display a STOP sign) Write a program that displays a STOP sign, as
shown in Figure 3.5b. The hexagon is in red and the text is in white.
'''

import turtle

turtle.begin_fill()
turtle.color("red")
turtle.circle(100, steps = 6)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-50, 80)
turtle.color("white")
turtle.write("STOP", font = ("Times", 30, "bold"))
turtle.end_fill()

turtle.hideturtle()
turtle.done()