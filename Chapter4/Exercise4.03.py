# Algebra: solve linear equations

# Prompt the user to enter a, b, c, d, e, and f
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

# Compute x and y and display the result
if (a * d - b * c) == 0:
    print("The equation has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(f"x is {format(x, "0.1f")} and y is {format(y, "0.1f")}")
