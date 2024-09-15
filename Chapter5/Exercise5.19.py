import sys

# Prompt the user to enter an integer between 1 to 15
number = int(input("Enter an integer (1 to 15): "))
count = 1
spaces = number * 3

# Ensure the number is within the valid range
if 1 <= number <= 15:
    # Loop to create each row of the pyramid
    for i in range(number + 1):
        # Print leading spaces for symmetry
        print(' ' * spaces, end='')
        # Print descending numbers
        for k in range(1, count - 1):
            print(-k + i + 1, end=' ')
        # Print ascending numbers
        for j in range(1, count):
            print(j, end=' ')
        count += 1
        if i <= 9:
            spaces -= 2
        else:
            spaces -= 3
        # Move to the next line after each row
        print()
else:
    print("Please enter a valid integer between 1 and 15.")
