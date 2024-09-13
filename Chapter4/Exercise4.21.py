# A program that prompts the user to enter a year, month, and day of the month 
# And then it displays the name of the day of the week.
import sys
import math

year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day_of_the_month = int(input("Enter the day of the month: 1-31: "))

m = month
if month == 1:
    m = 13
    year -= 1
elif month == 2:
    m = 14
    year -= 1

k = year % 100
j = math.floor(year / 100)
q = day_of_the_month
h = (q + (26 * (m + 1) /10) // 1 + k + (k / 4) // 1 + (j / 4) // 1 + 5 * j) % 7
if h == 0:
    print("Day of the week is Saturday.")
elif h == 1:
    print("Day of the week is Sunday.")
elif h == 2:
    print("Day of the week is Monday.")
elif h == 3:
    print("Day of the week is Tuesday.")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday.")
elif h == 6:
    print("Day of the week is Friday.")
else:
    print("Error")
