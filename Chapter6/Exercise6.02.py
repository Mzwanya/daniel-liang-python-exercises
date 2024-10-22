def sumDigits(n):
    sum = 0
    while n > 0:
        n1 = n % 10
        sum += n1
        n = n // 10

    return sum

n = eval(input("Enter an integer: "))
print("The sum of the digits is", sumDigits(n))
