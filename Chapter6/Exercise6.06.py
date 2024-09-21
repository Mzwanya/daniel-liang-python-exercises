def displayPattern(n):
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(format(" ", "2s"), end=" ")
        for j in range(i, 0, -1):
            print(format(j, "2d"), end=" ")
        print()


n = eval(input("Enter an integer: "))
displayPattern(n)
