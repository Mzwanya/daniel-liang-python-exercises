'''
5.4 (Conversion from miles to kilometers) Write a program that displays the following
table (note that 1 mile is 1.609 kilometers):
'''
count = 0
miles = 1
kilometers = 0
print("Miles        Kilomesters")
while count < 10:
    kilometers = miles * 1.609
    print(format(miles, "2.0f"), format(kilometers, '15.3f'))
    miles += 1
    count += 1

