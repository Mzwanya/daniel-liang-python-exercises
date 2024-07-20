'''
*2.18 (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the specified time zone.
'''
import time

total_seconds = int(time.time())
current_second = total_seconds % 60

total_minutes = total_seconds // 60
current_minute = total_minutes % 60

total_hours = total_minutes // 60
current_hour = total_hours % 24

timezone_offset_toGMT = eval(input("Enter the time zone offset to GMT: "))


print("The current time is", current_hour + timezone_offset_toGMT, ":", current_minute,  ":",  current_second)
