# Financial Application: compare costs

weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

# Compute the price per kilogram for each package
price_per_kilo1 = price1 / weight1
price_per_kilo2 = price2 / weight2

# Compute and display a better package
if price_per_kilo1 == price_per_kilo2:
    print("Both packages have better prices.")
elif price_per_kilo1 > price_per_kilo2:
    print("Package 1 has a better price.")
else:
    print("Package 2 has a better price.")
