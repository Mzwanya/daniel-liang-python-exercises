import turtle

# Displaying 9:15:00 under the clock
turtle.penup()
turtle.goto(-15, -165)
turtle.pendown()
turtle.write("9:15:00")

# Drawing the circle with radius = 150
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(150)

# Drawing 12, 9, 6 & 3 on the clock
turtle.penup()
turtle.goto(0, 137)
turtle.pendown()
turtle.write(12)

turtle.penup()
turtle.goto(-145, 0)
turtle.pendown()
turtle.write(9)

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.write(6)

turtle.penup()
turtle.goto(145, 0)
turtle.pendown()
turtle.write(3)

# Drawing the minnute-hand on the clock
turtle.penup()
turtle.left(90)
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(120)

# Drawing the hour-hand on the clock
turtle.penup()
turtle.right(90)
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(80)

turtle.done()
