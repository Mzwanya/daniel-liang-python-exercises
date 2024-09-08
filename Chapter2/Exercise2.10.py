# Find runway length

# Prompt the user to input speed and acceleration
speed = eval(input("Enter speed: "))
acceleration = eval(input("Enter acceleration: "))

# Calculate the runway length
length = (speed  ** 2) / (2 * acceleration)

# Display the results
print("The minimum runway length for this airplane is", int(round(length * 1000)) / 1000.0, "meters")
