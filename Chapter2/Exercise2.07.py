# Find the number of years and days from minutes

# Prompt the user to enter the number of minutes
minutes = eval(input("Enter the number of minutes: "))

# Compute the total number of minutes in a year and a day
total_minutes_in_one_year = 365 * 24 * 60
total_minutes_in_one_day = 24 * 60

# Compute years and days from the given minutes
years = minutes // total_minutes_in_one_year
remaining_minutes = minutes % total_minutes_in_one_year
days = remaining_minutes // total_minutes_in_one_day

# Display the results
print(minutes, "minutes is approximately", years, "years and", days, "days.")
