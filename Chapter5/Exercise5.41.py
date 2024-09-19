# Initialize max_num to a very small number and count to 0
max_num = float('-inf')
count = 0

# Continuously prompt the user for input
while True:
    # Prompt the user to enter a number
    number = int(input("Enter a number (0: for end of input): "))

    # End the loop if the input is 0
    if number == 0:
        break

    # Check if the number is greater than the current maximum number
    if number > max_num:
        max_num = number  # Update max_num to the new largest number
        count = 1  # Reset the count for the new largest number
    elif number == max_num:
        count += 1  # Increment the count if the same number is entered

# Display the result
print(f"The largest number is {max_num}")
print(f"The occurrence count of the largest number is {count}")
