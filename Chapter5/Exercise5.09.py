# Initial tuition fee for the current year
tuition = 10_000
rate_change = 0.05  # 5% increase
years = 0

# Compute the tuition after 10 years
while years < 10:
    tuition += tuition * rate_change
    years += 1
print("tuition in 10 years " + "$" + format(tuition, ".2f"))

# Compute the total cost for 4 years starting 10 years from now
total_cost = 0
years = 0
while years < 4:
    total_cost = tuition
    tuition += tuition * rate_change
    years += 1
print("The total cost of fours' worth tuition after ten years from now: " + "$" + format(tuition, ".2f"))
