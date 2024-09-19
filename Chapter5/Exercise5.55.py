import turtle

turtle.speed(0)  # Set the fastest drawing speed
turtle.penup()
turtle.goto(-150, 120)  # Move to the starting position
turtle.left(45)  # Rotate to draw the squares at an angle
turtle.pendown()

# Variable to track the color of the squares
is_black = False

# Draw the 8x8 grid of squares
for row in range(1, 9):
    for col in range(1, 9):
        turtle.begin_fill()  # Start filling the square

        # Draw a square by creating a circle with 4 steps (sides)
        turtle.circle(30, steps=4)

        # Alternate colors between black and white
        if is_black:
            turtle.color("black")
        else:
            turtle.color("white")
        
        is_black = not is_black  # Toggle color for the next square

        turtle.end_fill()  # Complete filling the square

        # Move to the next square in the same row
        turtle.penup()
        turtle.goto(turtle.xcor() + 42, turtle.ycor())
        turtle.pendown()

    # Move to the start of the next row
    turtle.penup()
    turtle.goto(-150, turtle.ycor() - 42)
    turtle.pendown()

    # Toggle the starting color for the next row
    is_black = not is_black

# Draw the outer black square
turtle.penup()
turtle.left(180)  # Reset the heading
turtle.goto(-192, 161)  # Move to the position for the outer square
turtle.color("black")
turtle.pensize(6)  # Set the pen size for the outer square
turtle.pendown()

# Draw a larger square by creating a circle with 4 steps (sides)
turtle.circle(240, steps=4)

turtle.hideturtle()
turtle.done()  # Finish drawing
