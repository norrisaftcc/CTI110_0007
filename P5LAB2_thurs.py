# Define your function here.
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    """ input: miles driven, miles per gallon, cost per gallon ($)
        returns: cost to drive that many miles
    """
    # Step 1: How many gallons of gas used?
    gas_used = driven_miles / miles_per_gallon # unit is "gallons"
    
    # Step 2: Cost for that much gas?
    cost = gas_used * dollars_per_gallon
    return cost

if __name__ == '__main__':
    # Type your code here.
    # we need miles, miles per gallon, and dollars per gallon
    # Program automatically checks for 10, 50, and 400 miles.
    #miles = float(input()) # miles driven
    MPG = float(input())   # miles per gallon
    DPG = float(input())   # cost ($) per gallon
    
    milesToTest = [10, 50, 400] #use a list to test these 
    
    for miles in milesToTest:
        cost = driving_cost(miles, MPG, DPG)
        print(format(cost, ".2f"))
    

    


