import turtle

# Lift the pen to move without drawing
turtle.penup()

# Move to the starting position at (-170, 150)
turtle.goto(-170, 150)

# Place the pen down to start drawing
turtle.pendown()

# Outer loop for rows (1 to 10)
for i in range(1, 11):
    # Inner loop for printing numbers in each row
    for j in range(1, i + 1):
        # Write the current number in bold, size 18 font
        turtle.write(str(j), font=("Times", 18, "bold"))
        
        # Lift the pen to move to the next number without drawing
        turtle.penup()
        
        # Move forward to the next position for the next number
        turtle.forward(30)
        
        # Place the pen down to write the next number
        turtle.pendown()
    
    # After each row, lift the pen to move down without drawing
    turtle.penup()
    
    # Move to the starting position for the next row, with the y-coordinate decreasing by 40
    turtle.goto(-170, turtle.ycor() - 40)
    
    # Place the pen down again to start writing the next row
    turtle.pendown()

turtle.hideturtle()
turtle.done()
