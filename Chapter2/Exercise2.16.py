# Acceleration

# Reading in v0, v1 and t
v0, v1, t = eval(input("Enter v0, v1, and t: "))

# compute average acceleration
average_acceleration = (v1 - v0) / t

# Display the results
print("The average acceleration is", int(round(average_acceleration * 10000)) / 10000.0)
