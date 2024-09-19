limit = 10_000  # Initial limit for the calculation

while limit <= 100_000:
    summation = 0  # Initialize summation variable

    # Calculate the approximation of PI using the series
    for i in range(1, limit + 1):
        summation += ((-1) ** (i + 1)) / (2 * i - 1)

    pi = 4 * summation  # Compute PI from the summation
    print(f"For i = {limit}, PI is approximately:", pi)  # Output the result
    
    limit += 10_000  # Increment the limit for the next iteration

