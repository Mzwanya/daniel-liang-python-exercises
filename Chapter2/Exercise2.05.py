# Financial application: calculate tips

# Prompting the user to enter the subtotal and the gratuity rate
subtotal = eval(input("Enter the subtotal: "))
gratuity_rate = eval(input("Enter the gratuity rate: "))

# Computing the gratuity and the total
gratuity = subtotal * gratuity_rate / 100
total = subtotal + gratuity

# Displaying the results
print("The gratuity is", int(gratuity * 100) / 100.0, "and the total is", int(total * 100) / 100.0)
