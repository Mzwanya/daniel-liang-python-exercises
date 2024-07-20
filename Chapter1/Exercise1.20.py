'''
(Turtle: display a rectanguloid) Write a program that displays a rectanguloid, as
shown in Figure 1.20b
'''
import turtle

# first rectangle with center at (0, 0)
turtle.goto(300, 0)
turtle.goto(300, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)

# second rectangle with center at (50, 50)
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.goto(350, 50)
turtle.goto(350, 150)
turtle.goto(50, 150)
turtle.goto(50, 50)

# Joining the vertices of each rectangle to the responding vertices of the other rectangle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(50, 50)

turtle.penup()
turtle.goto(300, 100)
turtle.pendown()
turtle.goto(350, 150)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(50, 150)

turtle.penup()
turtle.goto(300, 0)
turtle.pendown()
turtle.goto(350, 50)

turtle.done()