# Compute the perimeter of a triangle

# Prompt the user to enter three edges of a triangle
side1, side2, side3 = eval(input("Enter three edges (seperated with commas e.g. 1, 2, 3): "))

# Compute perimeter if the input is valid and display the result
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    perimeter = side1 + side2 + side3
    print("The perimter is", perimeter)
else:
    print("Invalid input")
