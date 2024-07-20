'''
2.22 (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
number of years and displays the population after that many years.
'''

# TO BE DONE LATER









'''
# OR USING A FOR LOOP:

current_population = 312032486
one_birth_per_seconds = 7
one_death_per_seconds = 13
one_immigrant_per_seconds = 45
one_year_in_seconds = 365 * 24 * 60 * 60

total_births_per_year = one_year_in_seconds // one_birth_per_seconds
total_deaths_per_year = one_year_in_seconds // one_death_per_seconds
total_immigrants_per_year = one_year_in_seconds // one_immigrant_per_seconds

change_in_population =  total_births_per_year + total_immigrants_per_year - total_deaths_per_year
number_of_years = eval(input("Enter number of years: "))

year = 1
for i in range(number_of_years):
    population = current_population + change_in_population
    # print(f"Year {year} population: ", population)
    year +=1
    current_population = population
print(f"Year {number_of_years} population is {current_population}")
'''