import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Adjust screen size for better view
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed
drawer.penup()

# Define the rectangle dimensions and center
rect_width = 120
rect_height = 100
center_x = 0
center_y = 0

# Draw the rectangle (for visualization)
drawer.goto(center_x - rect_width / 2, center_y - rect_height / 2)
drawer.pendown()
for _ in range(2):
    drawer.forward(rect_width)
    drawer.left(90)
    drawer.forward(rect_height)
    drawer.left(90)
drawer.penup()

# Draw 10 random balls
num_balls = 10
for _ in range(num_balls):
    # Generate random position within the rectangle
    x = random.uniform(center_x - rect_width / 2 + 10, center_x + rect_width / 2 - 10)
    y = random.uniform(center_y - rect_height / 2 + 10, center_y + rect_height / 2 - 10)
    
    # Draw a ball at the random position
    drawer.goto(x, y - 10)  # Move to the position
    drawer.pendown()
    drawer.color("black")  # Color of the ball
    drawer.begin_fill()
    drawer.circle(5)  # Draw a circle with radius 10
    drawer.end_fill()
    drawer.penup()

# Hide the turtle and display the result
drawer.hideturtle()
turtle.done()
