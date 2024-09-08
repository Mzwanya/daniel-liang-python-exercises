# Computing the volume of a cylinder

PI =  3.14159 # Constant pi

# Prompting the user to enter the radius and length of the cylinder
radius = eval(input("Enter the radius of a cylinder: "))
length = eval(input("Enter the length of the cylinder: "))

# Calculating the area and volume
area = radius * radius * PI
volume = area * length

# Displaying the results
print('The area is', area)
print("The volume is", volume)
