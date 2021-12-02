# CTI 110
# P3T1 - Are they 21?
# Name
# Date

# Check to see if the user is allowed to buy
# an adult beverage.

#age = int(input("How old is the customer? "))

# ask the customer's birth year
birthYear = int(input("What is customer's year of birth? "))
CURRENT_YEAR = 2021     # ALL CAPS means a constant (do not change)
# calculate their age
age = CURRENT_YEAR - birthYear


if age > 21:
    print("Purchase is allowed.")
    if age > 65:
        print("Also, they get a senior discount!")
        
elif age < 21:  # elif means "else if"
    print("Purchase is prohibited.")
else:           # customer is exactly 21
    print("Customer is exactly 21 - check birthday against today's date")


letter = input("Enter a letter: ")
# convert it to lowercase
letter = letter.lower()

if letter == "a" :
    print("Alpha")
elif letter == "b":
    print("Bravo")
else:
    print("Sorry... I only got as far as B")
