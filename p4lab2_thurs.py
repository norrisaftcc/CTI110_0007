# CTI 110
# P4T2
# Time Card
# Name
# Date

# This program will act like a time card reader,
# adding up each day's hours to get the total.

# Version 1 - uses numbers for days
# change line below if it's a 7 day week
DAYS_IN_WEEK = 5
totalHours = 0 #  the total starts at zero

print("Please enter your hours worked.")

for day in range(DAYS_IN_WEEK):
    print("Hours for day", day+1, ": ", end="")
    hoursToday = float(input())
    totalHours = totalHours + hoursToday # add to running total

# print the total
print("You worked a total of", totalHours, "hours this week.")

# print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")














# Version 2 - using names of the days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
totalHours = 0 #  the total starts at zero

print("Please enter your hours worked.")

for day in days:
    print("Hours for", day, ": ", end="")
    hoursToday = float(input())
    totalHours = totalHours + hoursToday # add to running total

# print the total
print("You worked a total of", totalHours, "hours this week.")

# print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")
