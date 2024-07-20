'''
**4.19 (Compute the perimeter of a triangle) Write a program that reads three edges for a
triangle and computes the perimeter if the input is valid. Otherwise, display that
the input is invalid. The input is valid if the sum of every pair of two edges is
greater than the remaining edge. Here is a sample run:
'''
side1, side2, side3 = eval(input("Enter three edges (seperated with commas e.g. 1, 2, 3): "))

perimeter = side1 + side2 + side3

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The perimter is", perimeter)
else:
    print("Invalid input")