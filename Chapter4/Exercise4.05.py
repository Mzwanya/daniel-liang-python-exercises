# Find future dates

# Prompt the user to enter an integer for today’s day of the week
todays_day_number = int(input("Enter today's day: "))

# Determine the day i.e. Sunday is 0, Monday is 1, ..., and Saturday is 6
todays_day = ''
if todays_day_number == 0:
    todays_day = 'Sunday'
elif todays_day_number == 1:
    todays_day = 'Monday'
elif todays_day_number == 2:
    todays_day = 'Tuesday'
elif todays_day_number == 3:
    todays_day = 'Wednesday'
elif todays_day_number == 4:
    todays_day = 'Thursday'
elif todays_day_number == 5:
    todays_day = 'Friday'
elif todays_day_number == 6:
    todays_day = 'Saturday'
else:
    todays_day = 'invalid input'

if todays_day == 'invalid input':
    print("Enter a valid day integer between 0 and 6")
else:
    # Prompt the user to enter the number of days after today for a future day
    number_of_days_elapsed = int(input("Enter the number of days elapsed since today: "))
    future_day = (todays_day_number + number_of_days_elapsed) % 7
    day = ''

# Determine the day ie Sunday is 0, Monday is 1, ..., and Saturday is 6
    if future_day == 0:
        day = 'Sunday'
    elif future_day == 1:
        day = 'Monday'
    elif future_day == 2:
        day = 'Tuesday'
    elif future_day == 3:
        day = 'Wednesday'
    elif future_day == 4:
        day = 'Thursday'
    elif future_day == 5:
        day = 'Friday'
    else:
        day = 'Saturday'

    print(f"Today is {todays_day} and the future day is {day}")