'''
**4.21 (Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week...
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday,
4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is the month (3: March, 4: April, ..., 12: December). January and February are
counted as months 13 and 14 of the previous year.
■ j is the century (i.e.,[ year/100].
■ k is the year of the century (i.e., year % 100).
Write a program that prompts the user to enter a year, month, and day of the
month, and then it displays the name of the day of the week.
'''

year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day_of_the_month = int(input("Enter the day of the month: 1-31: "))
m = 0
k = year % 100
j = (year / 100) // 1
if month == 1:
    m = 13
    year -= 1
    j = (year / 100) // 1
    k = year % 100
elif month == 2:
    m = 14
    year -= 1
    j = (year / 100) // 1
    k = year % 100
elif month == 3:
    m = 3
elif month == 4:
    m = 4
elif month == 5:
    m = 5
elif month == 6:
    m = 6
elif month == 7:
    m = 7
elif month == 8:
    m = 8
elif month == 9:
    m = 9
elif month == 10:
    m = 10
elif month == 11:
    m = 11
elif month == 12:
    m = 12
else:
    print("Error: Invalid input")

q = day_of_the_month

h = (q + (26 * (m + 1) /10) // 1 + k + (k / 4) // 1 + (j / 4) // 1 + 5 * j) % 7
if h == 0:
    day = 'Saturday'
    print("Day of the week is", day)
elif h == 1:
    day = 'Sunday'
    print("Day of the week is", day)
elif h == 2:
    day = 'Monday'
    print("Day of the week is", day)
elif h == 3:
    day = 'Tuesday'
    print("Day of the week is", day)
elif h == 4:
    day = 'Wednesday'
    print("Day of the week is", day)
elif h == 5:
    day = 'Thursday'
    print("Day of the week is", day)
elif h == 6:
    day = 'Friday'
    print("Day of the week is", day)
else:
    print("Error")

