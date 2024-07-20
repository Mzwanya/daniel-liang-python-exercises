import turtle

radius = eval(input("Enter the radius of the rings: "))

turtle.pensize(10)
turtle.penup()
turtle.goto(-110 - radius, -25)
turtle.color("blue")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(0, -25)
turtle.color("black")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(110 + radius, -25)
turtle.color("red")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-55 - radius, -75)
turtle.color("yellow")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(55 + radius, -75)
turtle.color("green")
turtle.pendown()
turtle.circle(radius)
turtle.done()
