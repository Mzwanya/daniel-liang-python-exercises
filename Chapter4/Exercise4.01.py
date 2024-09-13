# Algebra: solve quadratic equations

import math  # import the math module

# Prompt the user to enter a, b, c
a, b, c = eval(input("Enter a, b, c : "))

# Compute discriminant
discriminant = math.pow(b, 2) - 4 * a * c

# Compute the root/s based on the discriminant and display the result
if discriminant > 0:
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"The roots are {r1} and {r2}")
elif discriminant == 0:
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"The root is {r1}")
else:
    print("The equation has no real roots.")
