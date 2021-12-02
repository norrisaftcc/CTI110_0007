# CTI 110
# P4LAB2 - Password Checker
# Name
# Date

# PART 1
# Check if password is 8+ characters

# Declare variables
isPasswordOK = False
MIN_PW_LENGTH = 8 # constant

while False == isPasswordOK:
    # User chooses a password
    password = input("Please enter password: ")
    # We check it for length (and maybe other things)
    # If it's long enough... move on
    if len(password) >= MIN_PW_LENGTH:
        isPasswordOK = True
    # Otherwise loop again
    else:
        print("Password must be", MIN_PW_LENGTH, "or more characters.")

# End of loop
print("Your new password is:", password)

# PART 2
# TODO (Swap some characters to make it harder to guess)
# see Zybooks 11.16 for details

"""
replace characters using the key below,
and by appending "!" to the end of the input string.
    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $
"""
characters = list(password) # list of each char in password
newPassword = ""
for char in characters:
    #print(char) # testing
    if char == "i":
        char = "1" # i -> 1
    if char == "a":
        char = "@"
    if char == "m":
        char = "M"
    if char == "B":
        char = "8"
    if char == "s":
        char = "$"
    # Add the character (changed or not) to the new password
    newPassword += char
# end of loop
print("Your modified password is:", newPassword)





