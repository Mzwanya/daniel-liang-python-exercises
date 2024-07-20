'''
**5.9 (Financial application: compute future tuition) Suppose that the tuition for a university is $10,000
this year and increases 5% every year. Write a program that
computes the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now.
'''
tuition = 10_000
rate_change = 0.05
years = 1
while years <= 10:
    tuition += tuition * rate_change
    years += 1
print("tuition in 10 years", format(tuition, ".2f"))

total_cost = 0
years = 0
while years < 4:
    total_cost = tuition
    tuition += tuition * rate_change
    years += 1
print("The total cost of fours' worth tuition after ten years from now: " + format(total_cost, ".2f"))