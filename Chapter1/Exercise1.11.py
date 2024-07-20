# A program to estimate Population projection in a five year period

# TO BE DONE LATER. SEARCH TO FIND THE ARITHMETIC FORMULA FOR SIMPLIFY THE PROBLEM (Check Section2.11_2.22.py file)

current_population = 312032486
one_birth_per_seconds = 7
one_death_per_seconds = 13
one_immigrant_per_seconds = 45
one_year_in_seconds = 365 * 24 * 60 * 60

total_births_per_year = one_year_in_seconds // one_birth_per_seconds
total_deaths_per_year = one_year_in_seconds // one_death_per_seconds
total_immigrants_per_year = one_year_in_seconds // one_immigrant_per_seconds

change_in_population =  total_births_per_year + total_immigrants_per_year - total_deaths_per_year

year_one_population = current_population + change_in_population
current_population = year_one_population

year_two_population = current_population + change_in_population
current_population = year_two_population

year_three_population = current_population + change_in_population
current_population = year_three_population

year_four_population = current_population + change_in_population
current_population = year_four_population

year_five_population = current_population + change_in_population

print("Fisrt_year_population :", year_one_population)
print("Second_year_population:", year_two_population)
print("Third_year_population:", year_three_population)
print("Fourth_year_population:", year_four_population)
print("Fifth_year_population:", year_five_population)

'''
previous results
Fisrt_year_population : 314812582
Second_year_population: 317592678
Third_year_population: 320372774
Fourth_year_population: 323152870
Fifth_year_population: 325932966

'''
