# CTI 110
# P4LAB3 - Menu
# Name
# Date

# The idea here is to make a simple menu we can reuse.

# For this program, we'll be making a menu with 4 or more options. One of the options should be "Quit".

# If the user makes a choice other than those listed, they are asked to make the choice again.
# Once the user picks a menu option, print a message specific to that choice,
# and then return to the main menu.

# Program Start
choice = 0          # store the menu choice here
keepGoing = True    # loop until this is turned off

while keepGoing == True:
    print()
    print("Main menu.")
    print("_" * 10)
    print("1. Option 1") # change these for your program
    print("2. Option 2") 
    print("3. Option 3")
    print("4. Quit")

    #choice = int(input("Choose: ")) # original version
    try:
        choice = int(input("Choose: "))
        # still crashes if they type a non number...
        # Optional - this is advanced
    except ValueError:
        print("You must enter a number.")
        choice = 0 # this will just print another error message
        # end optional part
    
    # Pick from options
    if choice == 1:
        #pass     # "pass" does nothing - replace with actual code
        print("You chose option 1.")
    elif choice == 2:
        print("You chose option 2.")
    elif choice == 3:
        print("You chose option 3.")
    elif choice == 4:
        # User picked "quit"
        keepGoing = False
        print("Exiting.")
    else:
        # Anything other than the menu options
        print(choice,"is not a valid option.")

# end of main loop
print("Goodbye!")
    

