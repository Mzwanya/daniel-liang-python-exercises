# Convert feet into meters

# Prompting the user to input a value in feets
feet = eval(input("Enter a value for feet: "))

# Converting the value in feets into meters
meters = feet * 0.305

# Display the results
print(feet, "feet is", int(meters * 10000) / 1000.0, "meters.")
