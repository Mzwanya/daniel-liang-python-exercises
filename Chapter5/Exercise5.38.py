import time  # Import the time module to use the sleep function for delaying execution

# Prompt the user to enter the number of seconds
seconds = eval(input("Enter the number of seconds: "))

# Loop as long as the seconds value is greater than 0
while seconds > 0:
    time.sleep(1)  # Pause the program for 1 second

    # Check if there is more than 1 second remaining
    if seconds > 1:
        # Display the number of seconds left with the word 'seconds'
        print(str(seconds) + " seconds remaining")
    else:
        # When only 1 second is left, display '1 second remaining' (singular)
        print("1 second remaining")

    seconds -= 1  # Decrease the seconds counter by 1 after each iteration

# After the loop ends (when seconds reaches 0), print "Stopped"
print("Stopped")
