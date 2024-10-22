def reverse(number):
    num = ""
    while number > 0:
        n1 = number % 10
        num = num + str(n1)
        number = number // 10

    return int(num)

# Return true if number is a palindrome
def isPalindrome(number):
    revNumber = reverse(number)
    return True if revNumber == number else False


num = eval(input("Enter a number: "))
print(isPalindrome(num))
