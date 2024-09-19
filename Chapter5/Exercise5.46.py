import math

# Define the constant for the number of inputs
NUM_COUNT = 10
total_sum = 0
square_sum = 0

# Prompt the user to enter ten numbers
print("Enter ten numbers: ", end='')

# Loop to get input and calculate sum and square sum
for i in range(NUM_COUNT):
    number = float(input())
    total_sum += number
    square_sum += number * number

# Calculate the mean
mean = total_sum / NUM_COUNT

# Calculate the standard deviation
std_deviation = math.sqrt((square_sum - total_sum * total_sum / NUM_COUNT) / (NUM_COUNT - 1))

# Print Out the mean and standard deviation
print("The mean is", mean)
print("The standard deviation is", std_deviation)
