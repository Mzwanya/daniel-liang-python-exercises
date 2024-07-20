'''
**3.16 (Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
hexagon, and octagon, as shown in Figure 3.6b. Note that the bottom edges of
these shapes are parallel to the x-axis. (Hint: For a triangle with a bottom line
parallel to the x-axis, set the turtle’s heading to 60 degrees.)
'''
import turtle

turtle.hideturtle()
turtle.pensize(10)
radius = 50
turtle.right(60)

# Draw a Triangle
turtle.penup()
turtle.goto(-220, -25)
turtle.color("blue")
turtle.pendown()
turtle.circle(radius, steps=3)

# Draw a Square
turtle.penup()
turtle.left(15)
turtle.goto(-110, -25)
turtle.color("black")
turtle.pendown()
turtle.circle(radius, steps=4)

# Draw a Pentagon
turtle.penup()
turtle.left(10)
turtle.goto(0, -25)
turtle.color("red")
turtle.pendown()
turtle.circle(radius, steps=5)

# Draw a Hexagon
turtle.left(5)
turtle.penup()
turtle.goto(110, -25)
turtle.color("yellow")
turtle.pendown()
turtle.circle(radius, steps=6)

# Draw a Heptagon
turtle.left(5)
turtle.penup()
turtle.goto(220, -25)
turtle.color("green")
turtle.pendown()
turtle.circle(radius, steps=7)

turtle.done()

