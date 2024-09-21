def reverse(number):
    num = ""
    while number > 0:
        n1 = number % 10
        num = num + str(n1)
        number = number // 10

    return num


num = eval(input("Enter a number: "))
print("The reverse of", num, "is", reverse(num))
