# CTI 110
# P3LAB1- Interstates
# Name
# Date

"""
Background:
Primary U.S. interstate highways are numbered 1-99.
Odd numbers (like the 5 or 95) go north/south, and evens
(like the 10 or 90) go east/west. Auxiliary highways are
numbered 100-999, and service the primary highway indicated
by the rightmost two digits. Thus, I-405 services I-5, and
I-290 services I-90.
"""

#Ask user for highway number
highway = int(input("Enter highway number: "))

# Given a highway number, indicate whether it is a primary or auxiliary highway.
# numbers from 1-99 are primary, 100-999 are aux

# One way: nested ifs
"""
if highway >= 1:
    if highway <= 99:
        print("I-",highway, "is a primary highway.")
    else: # highway is 100 or more
        if highway <= 999:
            print("I-",highway, "is a auxiliary highway.")

"""

isPrimary = True # we'll set it false if need be below
isValid   = True 
# Another way: logical operators
if highway >= 1 and highway <= 99:
    print("I-", highway, " is a primary highway.", sep="")

elif highway >= 100 and highway <= 999:
    print("I-", highway, " is an auxiliary highway.", sep="")
    isPrimary = False 
else:
    print(highway, "is not a valid highway number.")
    isValid = False
    # honestly, we could just exit here.


# If auxiliary, indicate what primary highway it serves.
# This is the low 2 digits (ex: 540 serves 40, 295 serves 95.)
# Using modulo (%) will probably work.
# only non-primary roads serve other roads
if isPrimary == False:   
    primary = highway % 100 # divide by 100 and just keep remainder
    print("It serves highway I-",primary, ".")

# Also indicate if the (primary) highway runs north/south or east/west.
# N/S is odd, E/W is even
# We can determine odd/even with modulo 2.
if isValid == True:
    # If it's not a valid highway we can skip this part
    if highway % 2 == 0:
        # it's even
        print("The highway goes east/west.")
    else:
        # it's odd
        print("The highway goes north/south.")


    
