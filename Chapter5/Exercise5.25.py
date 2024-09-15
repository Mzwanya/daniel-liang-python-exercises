# From right to left summation
n = 50_000
summation_from_right = 1 / n
while n > 1:
    summation_from_right += 1 / (n - 1)
    n -= 1

# From Left to right summation
n = 1
summation_from_left = 1
while n < 50_000:
    summation_from_left += 1 / (n + 1)
    n += 1
# Display the results
print("summation from right to left", summation_from_right)
print("summation from left to right", summation_from_left)
