# Area of a hexagon

# Prompt the user to input the length of the side
side_length = eval(input("Enter the side: "))

# Compute area
area = (3 * (3 ** 0.5) * side_length ** 2) / 2

# Display the results
print("The area of the hexagon is", int(round(area * 10000)) / 10000.0)
