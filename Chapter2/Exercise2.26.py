'''
**2.26 (Turtle: draw a circle) Write a program that prompts the user to enter the
center and radius of a circle, and then displays the circle and its area, as shown
in Figure 2.5
'''
import turtle

x, y = eval(input("Enter the cordinates of the Center of the Circle (x, y): "))
radius = eval(input("Enter the radius of the Circle: "))

turtle.penup()
turtle.goto(x, y)
area = radius * radius * 3.14158
turtle.write(area)
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()
