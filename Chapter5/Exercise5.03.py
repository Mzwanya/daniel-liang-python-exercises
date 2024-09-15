count = 0
kilogram = 1
pound = 0
print("Kilograms        Pounds")
while count < 100:
    pound = kilogram * 2.2
    print(format(kilogram, "2.0f"), format(pound, "-18.1f"))
    kilogram += 2
    count += 1
