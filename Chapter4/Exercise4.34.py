# Input a hexadecimal character
hex_char = input("Enter a hexadecimal character (0-9, A-F): ").upper()

# Check if the input is valid
if '0' <= hex_char <= '9':
    decimal_value = ord(hex_char) - ord('0')  # For '0' to '9', map to 0-9
elif 'A' <= hex_char <= 'F':
    decimal_value = ord(hex_char) - ord('A') + 10  # For 'A' to 'F', map to 10-15
else:
    print("Invalid input. Please enter a valid hexadecimal character (0-9, A-F).")
    exit()

# Display the corresponding decimal value
print(f"The decimal value for hexadecimal {hex_char} is {decimal_value}.")
