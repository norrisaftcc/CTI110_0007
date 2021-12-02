# CTI 110
# P1T3 - Receipt
# Name
# Date

# Print a restaurant receipt
# set up variables
mealCost = float(input("Enter cost of meal: "))
taxPct = 0.07                # 7% is 7 / 100
taxCost = mealCost * taxPct

totalCost = mealCost + taxCost

print("Thank you for Dining at the Python Cafe")
print("-" * 40)
print("Meal: $", format(mealCost, "10.2f") )
print("Tax:  $", format(taxCost, "10.2f") )
print("-" * 40)
print("Total:$", format(totalCost, "10.2f") )

if mealCost > 100:
    print("BIG SPENDER!!!!")
    print("$$$$$")
print("bye!")
    
