'''
 (Turtle: draw a line) Write a program that draws a red line connecting two points
(-39, 48) and (50, -50) and displays the coordinates of the two points
'''

import turtle

turtle.penup()
turtle.goto(-39, 48)
turtle.pendown()
turtle.write("-39, 48")

turtle.goto(50, -50)
turtle.write("50,-50")

turtle.done()