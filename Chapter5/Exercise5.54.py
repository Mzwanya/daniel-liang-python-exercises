import turtle

turtle.speed(0)  # Set the fastest drawing speed

# Draw a parabola (y = x^2) curve
scale_factor = 0.01  # Scaling factor for the parabola
x_min = -100  # Starting x value
x_max = 100   # Ending x value
x = x_min

# Move to the starting point of the curve
turtle.penup()
turtle.goto(x, scale_factor * x * x)
turtle.pendown()

# Draw the parabola curve from x_min to x_max
for x in range(x_min, x_max + 1):
    turtle.goto(x, scale_factor * x * x)

# Draw the X-axis
turtle.penup()
turtle.goto(-160, 0)  # Move to start of X-axis
turtle.pendown()
turtle.goto(160, 0)   # Draw the X-axis line

# Draw the Y-axis
turtle.penup()
turtle.goto(0, -80)  # Move to start of Y-axis
turtle.pendown()
turtle.goto(0, 80)   # Draw the Y-axis line

# Label the Y-axis
turtle.penup()
turtle.goto(0, 80)   # Position label at the top of the Y-axis
turtle.pendown()
turtle.write("Y")

# Label the X-axis
turtle.penup()
turtle.goto(180, -15)  # Position label to the right of the X-axis
turtle.pendown()
turtle.write("X")

# Draw arrows on the X-axis
turtle.penup()
turtle.goto(160, 0)  # Move to the end of X-axis
turtle.pendown()
turtle.setheading(150)  # Set direction for left arrow
turtle.forward(20)      # Draw left side of X-axis arrow

turtle.penup()
turtle.goto(160, 0)  # Move back to the end of X-axis
turtle.pendown()
turtle.setheading(-150)  # Set direction for right arrow
turtle.forward(20)       # Draw right side of X-axis arrow

# Draw arrows on the Y-axis
turtle.penup()
turtle.goto(0, 80)  # Move to the top of Y-axis
turtle.pendown()
turtle.setheading(240)  # Set direction for left arrow on Y-axis
turtle.forward(20)      # Draw left side of Y-axis arrow

turtle.penup()
turtle.goto(0, 80)  # Move back to the top of Y-axis
turtle.pendown()
turtle.setheading(-60)  # Set direction for right arrow on Y-axis
turtle.forward(20)      # Draw right side of Y-axis arrow

# Hide the turtle and finish drawing
turtle.hideturtle()
turtle.done()
