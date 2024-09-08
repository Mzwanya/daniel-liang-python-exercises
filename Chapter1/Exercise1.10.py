# Finding average speed

# Converting distance in kilometers to miles and, time from seconds and minutes to hours
distance_in_kilometers = 14
distance_in_miles = distance_in_kilometers / 1.6
minutes = 45
seconds = 30
total_time_in_minutes = minutes + seconds / 60
total_time_in_hours = total_time_in_minutes / 60

# Calculating average in miles per hour
average_speed = distance_in_miles / total_time_in_hours

print("Average speed in miles per hour:", average_speed)