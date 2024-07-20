'''
(Physics: acceleration)
'''
v0, v1, t = eval(input("Enter v0, v1, and t: "))

average_acceleration = (v1 - v0) / t

print("The average acceleration is", int(round(average_acceleration * 10000)) / 10000.0)
