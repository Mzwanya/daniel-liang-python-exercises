year = int(input("Enter a year: "))
first_day = int(input("Enter the first day of the year (0 = Sunday, 1 = Monday, ..., 6 = Saturday): "))

days_of_Month = 0
for month in range(1, 13):
    print("\t", end='')

    if month == 1:
        print("January", year)
        days_of_month = 31
    elif month == 2:
        print("February ", year)
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            days_of_month = 29
        else:
            days_of_month = 28
    elif month == 3:
        print("March", year)
        days_of_month = 31
    elif month == 4:
        print("April", year)
        days_of_month = 30
    elif month == 5:
        print("May", year)
        days_of_month = 31
    elif month == 6:
        print("June", year)
        days_of_month = 30
    elif month == 7:
        print("July", year)
        days_of_month = 31
    elif month == 8:
        print("August", year)
        days_of_month = 30
    elif month == 9:
        print("September", year)
        days_of_month = 31
    elif month == 10:
        print("October", year)
        days_of_month = 30
    elif month == 11:
        print("November", year)
        days_of_month = 31
    elif month == 12:
        print("December", year)
        days_of_month = 31

    print("ـــــــــــــــــــــــــــ   ")
    print("   Sun Mon Tue Wed Thu Fri Sat")
    for i in range(0, first_day):
        print(format(" ", "4s"), end='')

    for i in range(1, days_of_month + 1):
        if i < 10:
            print(format(" ", "1s"), format(i, "2d"), end='')
        else:
            print(format(" ", "1s"), format(i, "2d"), end='')

        if (i + first_day) % 7 == 0:
            print()

    print("\n")
    first_day = (first_day + days_of_month) % 7
