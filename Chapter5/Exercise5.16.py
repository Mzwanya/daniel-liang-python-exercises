'''
*5.16 (Compute the greatest common divisor) For Listing 5.8, another solution to find
the greatest common divisor of two integers n1 and n2 is as follows: First find d to
be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2
'''
gck = 1
n1 = int(input("Enter the fisrt integer: "))
n2 = int(input("Enter the second integer: "))
d = min(n1, n2)

while d > 1:
    if n1 % d == 0 and n2 % d == 0:
        print("The gcd is", d)
        break
    d -= 1
    if d == 1:
        print("There is no gcd between " + str(n1) + " and " + str(n2))