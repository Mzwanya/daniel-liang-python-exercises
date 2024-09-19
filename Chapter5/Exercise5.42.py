import random

# Total number of simulations
total_throws = 1_000_000

# Counters for odd regions (Region 1 and Region 3)
odd_region_count = 0

# Simulate throwing the dart
for _ in range(total_throws):
    # Generate random coordinates (x, y) in the range [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check which region the point falls into
    if x <= 0 and y <= 0:  # Region 1 (Odd)
        odd_region_count += 1
    elif x > 0 and y <= x:  # Region 3 (Odd)
        odd_region_count += 1

# Calculate the probability for odd-numbered regions
probability_odd = odd_region_count / total_throws

# Output the result
print(f"The probability of landing in an odd-numbered region is {probability_odd:.4f}")
