'''
**5.27 (Compute PI) You can approximate PI by using the following series:
pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1)^(i + 1)/(2i - 1))

Write a program that displays the value for i = 10000, 20000... and
100000
'''

limit = 10_000
while limit <= 100_000:
    summation = 0
    for i in range(1, limit + 1):
        summation += ((-1) ** (i + 1)) / (2 * i - 1)
    pi = 4 * summation
    print(f"For i = {limit}, PI is approximately:", pi)
    limit += 10_000
