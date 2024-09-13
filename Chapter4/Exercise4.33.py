# Input an integer between 0 and 15
decimal = int(input("Enter an integer between 0 and 15: "))

# Check if the input is in the valid range
if 0 <= decimal <= 15:
    # Convert the integer to hexadecimal
    if decimal < 10:
        hex_value = str(decimal)  # For values 0 to 9, the hex is the same as the decimal
    else:
        hex_value = chr(ord('A') + decimal - 10)  # For values 10 to 15, use 'A' to 'F'
    
    # Display the result
    print(f"The hexadecimal value for {decimal} is {hex_value}.")
else:
    print("Invalid input. Please enter an integer between 0 and 15.")
