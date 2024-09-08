
import turtle

x1, y1, x2, y2 = eval(input("Enter two points (x1, y1, x2, y2): "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

s = "(" + str(x1) + ", " + str(y1) + ")"
turtle.write(s)

turtle.goto(x2, y2)
s = "(" + str(x2) + ", " + str(y2) + ")"
turtle.write(s)

turtle.done()
