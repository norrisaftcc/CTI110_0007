# CTI 110
# P5T2 - Lists and Functions
# Name
# Date

"""
This assignment will have two parts:
- A function makeList() that will build a list from user input,
- A function displayList() that will print out a list that it is given.
In addition, we'll try:
A function just for getting user input, so that we can do all our
"input validation" in one place
Future expansions: Could add ability to enter numbers until user is done
(instead of a set amount)
"""

def makeListOfSize(maxItems):
    """ build a list from user input.
    Input: size of the list desired
    Returns: a list of user entered numbers
    """
    items = [] # empty list

    print("Enter",maxItems,"numbers, one per line.")
    for i in range(maxItems):
        num = getInt() # was: num = int(input())
        items.append(num)
    return items


def displayList(items):
    """ takes a list, and prints it out item by item.
    Input: A list
    Returns: nothing
    """
    for item in items:
        print(item)

def getInt():
    """ ask user for number.
    Input: Nothing
    Returns: an int """
    validInput = False # loop until we get good input
    while validInput == False:
        try:
            num = int(input("Enter a number: "))
            # if no exception, the input is good
            validInput = True
        except ValueError:
            print("That is not a valid integer, please try again.")
        
    # end of while
    return num

def removeDuplicates(myList):
    """ Convert list to set, then back to list.
        This removes all duplicate entries.
        Input: a list
        Returns: a list (without duplicates)
    """
    mySet = set(myList) # removes dupes
    myList = list(mySet)
    return myList

def findAverage(myList):
    """ Input: a list
        Returns: average of all items in list
        NOTE: don't use with an empty list (divide by zero)
    """
    total = 0
    numItems = len(myList)

    for num in myList:
        total = total + num

    average = total / numItems
    return average

def findMinandMax(myList):
    """ Input: a list of numbers
    Output: two values, the smallest number in the list
    and the largest"""

    minNum = min(myList) # find smallest
    maxNum  = max(myList) # find largest
    
    return minNum, maxNum

def main():
    print("Build a list.")
    sizeOfList = int(input("How many items? "))
    myList = makeListOfSize(sizeOfList)

    print("Now display it.")
    displayList(myList)
    myList = removeDuplicates(myList)
    print("With no duplicates:")
    displayList(myList)
    print("Finding average...")
    average = findAverage(myList)
    print("The average of these numbers is", average)

    print("Finding min and max values...")
    minNum, maxNum = findMinandMax(myList)
    print("min =", minNum, "max =", maxNum )
    
    print("Done.")

# start program
main()
