import math

number = 0
print("Number     Square Root")
while number <= 20:
    print(format(number, "2.0f"), format(math.sqrt(number), "15.4f"))
    number += 2
