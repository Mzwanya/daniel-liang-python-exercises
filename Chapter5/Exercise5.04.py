count = 0
miles = 1
kilometers = 0
print("Miles        Kilomesters")
while count < 10:
    kilometers = miles * 1.609
    print(format(miles, "2.0f"), format(kilometers, '15.3f'))
    miles += 1
    count += 1
