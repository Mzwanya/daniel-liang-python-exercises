# Find the number of days in a month

# Prompt the user to enter month and year
month, year = eval(input("Enter month, year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Determine the month and days
days = 0
if month == 1:
    month = "January"
    days = 31
elif month == 2:
    month = "February"
    if isLeapYear:
        days = 29
    else:
        days = 28
elif month == 3:
    month = "March"
    days = 31
elif month == 4:
    month = "April"
    days = 30
elif month == 5:
    month = "May"
    days = 31
elif month == 6:
    month = "June"
    days = 30
elif month == 7:
    month = "July"
    days = 31
elif month == 8:
    month = "August"
    days = 30
elif month == 9:
    month = "September"
    days = 31
elif month == 10:
    month = "October"
    days = 30
elif month == 11:
    month = "November"
    days = 31
elif month == 12:
    month = "December"
    days = 31

# Display the results
print(month, year, "has", days, "days")
