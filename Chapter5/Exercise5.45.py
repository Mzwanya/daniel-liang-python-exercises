# Prompt the user to enter an integer
input_number = int(input("Enter an integer: "))

# Initialize an empty string to store the hexadecimal representation
hex_representation = ""

# Store the value to be converted in a separate variable
current_value = input_number

# Convert the integer to hexadecimal
while current_value != 0:
    # Calculate the remainder when dividing by 16
    remainder = current_value % 16
    # Convert remainder to its hexadecimal character representation
    if remainder >= 10:
        hex_representation += chr(remainder + 55)  # Convert 10-15 to 'A'-'F'
    else:
        hex_representation += str(remainder)  # Convert 0-9 to corresponding digit

    # Use integer division to reduce the current_value
    current_value //= 16

# Reverse the hexadecimal representation string
reversed_hex = ""
for i in range(len(hex_representation) - 1, -1, -1):
    reversed_hex += hex_representation[i]

# Output the result
print("The hexadecimal representation of", input_number, "is", reversed_hex)
