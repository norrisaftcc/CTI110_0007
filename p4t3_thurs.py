# CTI 110
# P4T3 - Running Total
# Name
# Date

# For this program we're adding up numbers
currentNumber = 0 # we'll store each number here before adding
total = 0
numEntries = 0 # Ask user how many times to loop
count = 0 # Used to keep track of our loop


# We'll ask the user how many
# Test: let's validate this value (must be >0)
numEntries = int(input("How many numbers to add? "))
while numEntries <= 0:
    print("Please enter a value greater than zero.")
    numEntries = int(input("How many numbers to add? "))

# then loop and enter each number
while count < numEntries:
    #print("*count =", count, "numEntries =", numEntries) # debugging
    # enter each number
    #print("\t the count is", count) # just for testing
    currentNumber = int(input("Enter number: "))
    #total = total + currentNumber
    total += currentNumber
    #count = count + 1
    count += 1

# finally print the total.
print("The total is:", total)

# Can we find the average?
# We really should just not let numEntries be a "bad" value
if numEntries > 0:
    average = total / numEntries
    print("The average is:", average)


