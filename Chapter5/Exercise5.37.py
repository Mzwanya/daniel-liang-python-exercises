import math

sum = 0   # Initialize a variable to hold the summation result

# Loop through values from 1 to 624 (inclusive)
for i in range(1, 625):
    sum += 1 / (math.sqrt(i) + math.sqrt((i + 1)))
    
# After the loop ends, print the final summation result
print("The summation of the series is", sum)
