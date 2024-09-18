for i in range(3, 10000 + 1):
    sum = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            sum += j

    if sum == i:
        print(i)
