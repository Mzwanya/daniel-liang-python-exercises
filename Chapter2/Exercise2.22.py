# Population projection

# Prompt the user to enter the number of years
number_of_years = eval(input("Enter the number of years: "))

# Compute population in the given number of years
population = int(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * number_of_years))

# Display the results
print(f"The population in {number_of_years} years is", population)
