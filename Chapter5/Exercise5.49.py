import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()

# Define table parameters
cell_width = 40
cell_height = 30
start_x = -200  # Starting x-coordinate for the table
start_y = 150   # Starting y-coordinate for the table

# Draw the header: numbers 1 to 9 horizontally across the top
drawer.goto(start_x, start_y)
drawer.write("Multiplication Table", align="center", font=("Arial", 14, "bold"))

# Move down a bit for the number header row
drawer.goto(start_x + 40, start_y - 20)

for col in range(1, 10):
    x = start_x + col * cell_width
    drawer.goto(x, start_y - 30)
    drawer.write(col, align="center", font=("Arial", 12, "normal"))

# Draw the horizontal line under the header
drawer.goto(start_x, start_y - 40)
drawer.pendown()
drawer.forward(9 * cell_width + 10)
drawer.penup()

# Draw the left-side row headers (1 to 9) and the multiplication results
for row in range(1, 10):
    # Row header
    x = start_x
    y = start_y - 40 - row * cell_height
    drawer.goto(x, y)
    drawer.write(f"{row} |", align="right", font=("Arial", 12, "normal"))
    
    # Draw multiplication results
    for col in range(1, 10):
        x = start_x + col * cell_width
        drawer.goto(x, y)
        result = row * col
        drawer.write(f"{result:4}", align="center", font=("Arial", 12, "normal"))

# Hide the turtle and display the result
drawer.hideturtle()
turtle.done()
