# A program to estimate population projection in a five year period

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

print("First_year_population :", year_one_population)
print("Second_year_population:", year_two_population)
print("Third_year_population:", year_three_population)
print("Fourth_year_population:", year_four_population)
print("Fifth_year_population:", year_five_population)
