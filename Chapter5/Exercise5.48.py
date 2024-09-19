import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Adjust screen size for better view
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed
drawer.penup()

# Define the number of circles and the initial radius
num_circles = 10
initial_radius = 10
radius_increment = 10

# Draw 10 circles
for i in range(num_circles):
    # Calculate the radius for the current circle
    radius = initial_radius + i * radius_increment
    
    # Move to the start position (bottom of the circle)
    drawer.goto(0, -radius)
    drawer.pendown()
    
    # Draw the circle
    drawer.circle(radius)
    drawer.penup()

# Hide the turtle and display the result
drawer.hideturtle()
turtle.done()
