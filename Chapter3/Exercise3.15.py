'''
*3.15 (Turtle: paint a smiley face) Write a program that paints a smiley face, as shown in
Figure 3.6a
'''
import turtle

turtle.pensize(3)
turtle.speed(10)

# Draw the head (circle)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)

# Draw the eyes
turtle.penup()
turtle.begin_fill()
turtle.color("black")
turtle.goto(-85, 60)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.begin_fill()
turtle.color("black")
turtle.goto(85, 60)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()

# Draw the nose (n - shaped)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(-50, -40)

turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(50, -40)
# Draw the mouth (v - shaped)
turtle.penup()
turtle.goto(-120, -40)
turtle.pendown()
turtle.goto(0, -120)

turtle.penup()
turtle.goto(120, -40)
turtle.pendown()
turtle.goto(0, -120)
turtle.hideturtle()
turtle.done()

