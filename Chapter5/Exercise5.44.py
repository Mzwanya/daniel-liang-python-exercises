# Prompt the user to enter an integer
input_number = int(input("Enter an integer: "))

# Initialize an empty string to store the binary representation
binary_representation = ""

# Store the value to be converted in a separate variable
current_value = input_number

# Convert the integer to binary
while current_value != 0:
    # Prepend the remainder of current_value divided by 2 to the binary representation
    binary_representation = str(current_value % 2) + binary_representation
    
    # Use integer division to reduce the current_value
    current_value = current_value // 2

# Output the result
print("The binary representation of", input_number, "is", binary_representation)
