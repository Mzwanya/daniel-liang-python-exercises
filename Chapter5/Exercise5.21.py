limit = 9  # Define the number of lines
x = limit * 2  # Initialize spacing factor

for i in range(1, limit):
    s = limit + x  # Calculate space for alignment
    sp = str(s) + "s"  # Create format string for spacing
    print(format(" ", sp), end='')  # Print leading spaces

    # Print ascending powers of 2
    for j in range(0, i - 1):
        print(format(2**j, "3d"), end='')

    # Print descending powers of 2
    for j in range(i - 1, -1, -1):
        print(format(2**j, "3d"), end='')
    
    print()  # Move to the next line
    x -= 3  # Decrease spacing for the next line
