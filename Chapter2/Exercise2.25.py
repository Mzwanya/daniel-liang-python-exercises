'''
**2.25 (Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle, as shown in
Figure 2.4c
'''
import turtle

length = eval(input("Enter the length of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
x, y = eval(input("Enter the cordinates of the Center of the rectangle (x, y): "))

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.goto(x + length, y)
turtle.goto(x + length, y + width)
turtle.goto(x, y + width)
turtle.goto(x, y)

turtle.done()
