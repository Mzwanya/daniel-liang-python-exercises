def displaySortedNumbers(num1, num2, num3):
    max1 = max(num1, num2, num3)
    max2 = max3 = 0
    if max1 == num1:
        max2 = max(num2, num3)
        max3 = min(num2, num3)
    elif max1 == num2:
        max2 = max(num1, num3)
        max3 = min(num1, num3)
    else:
        max2 = max(num1, num2)
        max3 = min(num1, num2)

    print("The sorted numbers are", max3, max2, max1)


n1, n2, n3 = eval(input("Enter three numbers: "))
displaySortedNumbers(n1, n2, n3)
