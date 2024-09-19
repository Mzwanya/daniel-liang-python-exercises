import random

# Initialize counters for heads and tails
heads_count = 0
tails_count = 0

# Simulate flipping a coin one million times
for flip in range(1_000_000):
    # Randomly generate 0 (heads) or 1 (tails)
    flip_result = random.randint(0, 1)

    if flip_result == 0:
        heads_count += 1  # Increment heads count if result is 0
    else:
        tails_count += 1  # Increment tails count if result is 1

# Display the number of heads and tails
print(f"Number of heads: {heads_count}")
print(f"Number of tails: {tails_count}")
