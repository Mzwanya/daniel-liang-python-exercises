'''
**2.7 (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days.
'''
minutes = eval(input("Enter the number of minutes: "))

total_minutes_in_one_year = 365 * 24 * 60
total_minutes_in_one_day = 24 * 60

years = minutes // total_minutes_in_one_year
remaining_minutes = minutes % total_minutes_in_one_year
days = remaining_minutes // total_minutes_in_one_day

print(minutes, "minutes is approximately", years, "years and", days, "days.")

