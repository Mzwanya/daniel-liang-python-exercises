# Draw four hexagons

import turtle

# First hexagon
turtle.right(90)
turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

# Second hexagon
turtle.forward(100)
turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

# Third hexagon
turtle.right(60)
turtle.penup()
turtle.goto(20, -100)
turtle.pendown()

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

# Fourth hexagon
turtle.right(60)
turtle.forward(200)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.left(60)
turtle.forward(100)

turtle.hideturtle() # hide the turtle pen
turtle.done() # pause the turtle window
