# Prompt the user for the year and the first day of the year
year = int(input("Enter the year: "))
first_day_of_year = int(input("Enter the first day of the year (0 = Monday, 1 = Tuesday, ..., 6 = Sunday): "))

# Initialize the first day of the year
current_day = first_day_of_year

# Define month names and number of days in each month
for month in range(12):
    # Determine the month name
    if month == 0:
        month_name = "January"
    elif month == 1:
        month_name = "February"
    elif month == 2:
        month_name = "March"
    elif month == 3:
        month_name = "April"
    elif month == 4:
        month_name = "May"
    elif month == 5:
        month_name = "June"
    elif month == 6:
        month_name = "July"
    elif month == 7:
        month_name = "August"
    elif month == 8:
        month_name = "September"
    elif month == 9:
        month_name = "October"
    elif month == 10:
        month_name = "November"
    elif month == 11:
        month_name = "December"

    # Determine the day of the week
    if current_day == 0:
        day_name = "Monday"
    elif current_day == 1:
        day_name = "Tuesday"
    elif current_day == 2:
        day_name = "Wednesday"
    elif current_day == 3:
        day_name = "Thursday"
    elif current_day == 4:
        day_name = "Friday"
    elif current_day == 5:
        day_name = "Saturday"
    elif current_day == 6:
        day_name = "Sunday"

    # Print the first day of the month
    print(f"{month_name} 1, {year} is {day_name}")

    # Determine the number of days in the current month
    if month == 1:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29  # Leap year
        else:
            days = 28
    elif month == 3 or month == 5 or month == 8 or month == 10:  # April, June, September, November
        days = 30
    else:  # January, March, May, July, August, October, December
        days = 31

    # Update the current day for the next month
    current_day = (current_day + days) % 7
