# Initialize the starting value of e and the first term in the series (1/0! = 1)
e_value = 1 
term = 1

# Loop to calculate e for i from 1 to 100_000
for i in range(1, 100_000 + 1):
    term = term / i  # Calculate the next term in the series (1/i!)
    e_value += term  # Add the current term to the value of e

    # Print the value of e for specific values of i
    if i == 10_000 or i == 20_000 or i == 30_000 or i == 40_000 or \
       i == 50_000 or i == 60_000 or i == 70_000 or i == 80_000 or \
       i == 90_000 or i == 100_000:
        print("The value of e is " + str(e_value) + " for i = " + str(i))
