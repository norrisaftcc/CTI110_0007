# CTI 110
# P2T2 - Age Checker
# Name
# Date

# version 2 -
# Ask for customer birth date
# and then calculate the age
#age = int(input("How old is the customer? "))

CURRENT_YEAR = 2021
birthYear = int(input("What is the customer's birth year? "))
age = CURRENT_YEAR - birthYear
print(age) # this is a debug print statement

# Are they over 21, or not?
if age > 21:
    print("Purchase is allowed.")
elif age < 21:
    print("Purchase is prohibited.")
else:
    print("Customer is exactly 21 - check birth date against today's date.")

    
        
    
