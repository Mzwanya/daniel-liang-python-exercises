import turtle

turtle.speed(0)  # Set the fastest drawing speed
turtle.penup()
turtle.goto(-170, 150)  # Move to the starting position
turtle.pendown()

# Draw horizontal lines
for i in range(18):
    turtle.forward(170)
    turtle.penup()
    turtle.goto(-170, turtle.ycor() - 10)  # Move down 10 units
    turtle.pendown()

# Reset position and direction to draw vertical lines
turtle.penup()
turtle.goto(-170, 150)
turtle.pendown()
turtle.right(90)

# Draw vertical lines
for i in range(18):
    turtle.forward(170)
    turtle.penup()
    turtle.goto(turtle.xcor() + 10, 150)  # Move right 10 units
    turtle.pendown()

# Hide the turtle and finish the drawing
turtle.hideturtle()
turtle.done()
