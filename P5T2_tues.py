# CTI 110
# P5T2 - Lists and Functions
# Name
# Date

"""
Program has two parts:
makeList() - build a list from user entered values
displayList() - take a list, display each item
TODO: Maybe add input validation
"""


def getNumber():
    """
    input: none
    output: an int
    """
    goodInput = False # repeat until we get good input
    while goodInput == False:
        try:
            num = int(input("Enter a number: "))
            goodInput = True
        except ValueError:
            print("That is not a valid int... please try again.")
    return num

def makeListOfSize(size):
    """
    Makes a list from user entered numbers
    input: size (int) - length of the list
    returns: a list
    """
    newList = []
    for i in range(size): # repeats size times
        #num = int(input("Enter a number: "))
        num = getNumber()
        newList.append(num)
    return newList


def displayList(items):
    """
    Display a list of items.
    input: a list
    returns: none
    """
    for item in items:
        print(item, end=" ")
    print() # end of line

def removeDupes(items):
    """
    Take a list and remove duplicates (using set)
    input: a list
    returns: a list without duplicate entries
    """
    mySet = set(items)
    noDupeList = list(mySet)

    return noDupeList


def getMinandMaxOf(numbers):
    """
    input: a list
    returns: two numbers, the min and max values in list
    """
    minNum = min(numbers)
    maxNum = max(numbers)
    return minNum, maxNum

def getTotalAndAverage(numbers):
    """
    input: a list
    returns: two numbers, total and average of all values
    """
    total  = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return total, average

def main():
    #print("Making a list...")
    size = int(input("How many items in the list? "))
    numbers = makeListOfSize(size)
    print("Displaying list...")
    displayList(numbers)
    print("Removing duplicates...")
    numbersNoDupes = removeDupes(numbers)
    displayList(numbersNoDupes)
    # multiple variable return
    minNum, maxNum = getMinandMaxOf(numbers)
    print("Smallest =", minNum, "Largest =", maxNum)
    
    total, average = getTotalAndAverage(numbers)
    print("total =", total, "Average =", average)
    print("Done.")

# start
main()
