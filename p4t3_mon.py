# CTI 110
# P4T3 - Another Time Card Loop
# Name
# Date

# For this version, keep asking for values until
# the user enters -1

# use a boolean for the loop
keepGoing = True
total = 0
numDays = 0 # used for averaging

while keepGoing: # could say while keepGoing == True
    time = float(input("Enter hours worked this day, or -1 to exit: "))

    # If they choose -1, leave the loop
    if time == -1:
        print("Exiting.")
        keepGoing = False # We will exit the next time we hit "while"
        
    # Otherwise, add the time to the total
    else:
        total = total + time
        numDays = numDays + 1


# Loop is ended
print("You worked a total of", total, "hours this pay period.")

# TODO - can we add averages?
average = total / numDays
print("For an average of", average, "hours per day.")
