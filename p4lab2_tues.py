# CTI 110
# P4LAB2 - Password Strength Checker
# Name
# Date

# Part 1 - password length

# Declare variables
MIN_LENGTH = 8 # change if you want longer passwords
isGoodPassword = False

# until the user gives a good enough password:
while False == isGoodPassword:
    
    # ask user for password
    password = input("Please enter a new password: ")
    # check length
    # if it's at least MIN_LENGTH, it's a good password
    if len(password) >= MIN_LENGTH:
        #isGoodPassword = True
        # require upper and lower case
        # note we don't even check this until we have the length down
        if password == password.lower() or password == password.upper():
            print("Password should contain a mix of upper and lower case letters.")
        else:
            isGoodPassword = True
    
    # otherwise try again
    else:
        print("Password must be at least", MIN_LENGTH, "characters.")

# end of loop

print("Your new password is:",password)


# Part 2 - swapping characters
# (see 11.16)
# Notes:
"""
    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $
and add ! to the end
"""
print("Now we'll replace some characters to make it harder to guess.")
newPassword = "" # we will add each character one at a time
chars = list(password)

for char in chars:
    
    # if it's a character to replace, then replace it
    if char == "i":
        char = "1"
    if char == "a":
        char = "@"
    if char == "m":
        char = "M"
    if char == "B":
        char = "8"
    if char == "s":
        char = "$"
    #print(char) # testing
    newPassword += char # stick new character on the end

# finally add the ending "!"
newPassword += "!"

print("Your fancy new password is:", newPassword)


    















