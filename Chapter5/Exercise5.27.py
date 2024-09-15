limit = 10_000
while limit <= 100_000:
    summation = 0
    for i in range(1, limit + 1):
        summation += ((-1) ** (i + 1)) / (2 * i - 1)
    pi = 4 * summation
    print(f"For i = {limit}, PI is approximately:", pi)
    limit += 10_000
