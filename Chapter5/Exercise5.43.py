count = 0  # Initialize the counter for combinations

# Iterate through numbers for the first element of the pair
for i in range(1, 8):
    # Iterate through numbers for the second element of the pair
    for j in range(i + 1, 8):
        print(i, " ", j)
        count += 1  # Increment the combination count

# Print the total number of unique combinations
print("The total number of all combinations is", count)
