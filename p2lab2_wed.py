# CTI 110
# P2LAB2 - Caffeine
# Name
# Date


# Ask user for amount of the dose (caffeine in mg)
dose = float(input())

# TODO: fill in these numbers
doseAfter6 = 0
doseAfter12 = 0
doseAfter24 = 0

# Every 6 hours, the dose is half of the previous number.
doseAfter6 = dose / 2 # definition of half-life
doseAfter12 = doseAfter6 / 2
doseAfter18 = doseAfter12 / 2
doseAfter24 = doseAfter18 / 2


# TODO: Print answer out with formatting
#print(doseAfter6)
print(format(doseAfter6, ".2f"))
print(format(doseAfter12, ".2f"))
print(format(doseAfter24, ".2f"))



