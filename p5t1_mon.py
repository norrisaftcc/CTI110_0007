# CTI 110
# P5T1 - Menu Continued
# Name
# Date

# The idea here is to make a simple menu we can reuse.

# For this program, we'll be making a menu with 4 or more options. One of the options should be "Quit".

# If the user makes a choice other than those listed, they are asked to make the choice again.
# Once the user picks a menu option, print a message specific to that choice,
# and then return to the main menu.

# Utility functions
def printMenu():
    """ this function prints the main menu for the user to choose from.

    """
    print()
    print("Main menu at the fair...")
    print("_" * 10)
    print("1. Food Truck") # change these for your program
    print("2. Budget Escape Room") 
    print("3. Surprise")
    print("4. Leave the Fair")


# Functions for menu choices
# These are called from main
def doOption1():
    """
    option 1 is the food truck.
    The user can pick a meal and some toppings.
    Input: None
    Output: None
    Effect: Prints out the user's order
    """
    print("You chose the Food Truck.")
    # build the meal from the user choices
    meal = "" 
    choice = input("Do you go to the taco truck or the burger truck? ")
    if choice == "taco":
        meal += "taco"
    elif choice == "burger":
        meal += "burger"
    else:
        print("Well, if you don't pick either, I guess there's no point...")
        return # just leave the function
    choice = input("Do you want lettuce, tomatoes, both, or plain?")
    if choice == "lettuce" or choice == "both":
        meal += " with lettuce"
    if choice == "tomatoes" or choice == "both":
        meal += " add tomatoes"
    print("Here's your order!", meal)
    return # the normal exit

def doOption2():
    print("You chose the Budget Escape Room.")
    isPlaying = True
    while isPlaying:
        print("This is a budget escape room.")
        print("You are in a room with a closed door.")
        print("Do you open it? (y/n)" )
        answer = input()
        if answer == "y" or answer == "yes":
            print("You escaped! What a victory!")
            isPlaying = False
        else:
            print("Well, you're still here...")
    return # end of function

def doOption3():
    print("You chose option 3 - Surprise!")
    # put whatever here
    return 

# Main (and the main menu)
def main(): 
    # Program Start
    choice = 0          # store the menu choice here
    keepGoing = True    # loop until this is turned off

    while keepGoing == True:
        printMenu()

        choice = int(input("Choose: ")) # original version

        # Pick from options
        if choice == 1:
            doOption1()
        elif choice == 2:
            doOption2()
        elif choice == 3:
            doOption3()
        elif choice == 4:
            # User picked "quit"
            keepGoing = False
            print("Exiting.")
        else:
            # Anything other than the menu options
            print(choice,"is not a valid option.")

    # end of main loop
    print("Goodbye!")

# run program
main()

