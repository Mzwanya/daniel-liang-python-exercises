gck = 1
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
d = min(n1, n2)

while d > 1:
    if n1 % d == 0 and n2 % d == 0:
        print("The gcd is", d)
        break
    d -= 1
    if d == 1:
        print("There is no gcd between " + str(n1) + " and " + str(n2))
