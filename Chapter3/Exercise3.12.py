import turtle

length = eval(input("Enter the length of the star: "))
angle = 144

turtle.forward(length)
turtle.right(angle)

turtle.forward(length)
turtle.right(angle)

turtle.forward(length)
turtle.right(angle)

turtle.forward(length)
turtle.right(angle)

turtle.forward(length)
turtle.right(angle)

turtle.forward(length)
turtle.right(angle)

'''
# OR USING A FOR LOOP
for i in range(5):
    turtle.forward(length)
    turtle.right(angle)
'''

turtle.hideturtle()
turtle.done()
