'''
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
'''
PI =  3.14159
radius = eval(input("Enter the radius of a cylinder: "))
length = eval(input("Enter the length of the cylinder: "))
area = radius * radius * PI
volume = area * length

print('The area is', area)
print("The volume is", volume)
