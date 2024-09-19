# Iterate through numbers from 3 to 10,000
for i in range(3, 10_000 + 1):
    sum_of_divisors = 0  # Initialize sum of divisors

    # Find all divisors of the number i
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            sum_of_divisors += j

    # Check if the sum of divisors equals the number itself
    if sum_of_divisors == i:
        print(i)  # Print the number if it is a perfect number
