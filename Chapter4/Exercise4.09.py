'''
*4.9 (Financial: compare costs) Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the costs of the
packages. The program prompts the user to enter the weight and price of each
package and then displays the one with the better price.
'''

weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

weight_ratio = weight1 / weight2
price_ratio = price1 / price2

if weight_ratio == price_ratio:
    print("Both packages have better prices.")
elif weight_ratio > price_ratio:
    print("Package 1 has a better price.")
else:
    print("Package 2 has a better price.")