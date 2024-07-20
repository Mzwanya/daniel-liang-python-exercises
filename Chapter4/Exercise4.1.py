# *4.1 (Algebra: solve quadratic equations)
import math

a, b, c = eval(input("Enter a, b, c : "))

if (b * b - 4 * a * c) > 0:
    r1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    r2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print(f"The roots are {r1} and {r2}")
elif (b * b - 4 * a * c) == 0:
    r1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    print(f"The root is {r1}")
else:
    print("The equation has no real roots.")