# 2.15 (Geometry: area of a hexagon)

side_length = eval(input("Enter the side: "))

area = (3 * (3 ** 0.5) * side_length * side_length) / 2

print("The area of the hexagon is", int(round(area * 10000)) / 10000.0)


