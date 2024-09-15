# Initialize the starting year and ending year
start_year = 2001
end_year = 2100

# Initialize a counter for how many leap years have been printed on the current line
count = 0

# Iterate over the range of years
for year in range(start_year, end_year + 1):
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Print the year, followed by a space
        print(year, end=' ')
        count += 1
        # Print a new line after every 10 years
        if count % 10 == 0:
            print()
