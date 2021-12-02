# CTI 110
# P5T3 - Random Numbers
# Name
# Date

# This program shows off a few different ways to get random results.

import random
# we can now use random.randint() and other calls
# abbrev: 1d6 - a six sided die, 2d6 - two six sided dice, etc.



def rollDie():
    """ input: none
        output: number from 1-6
    """
    result = random.randint(1, 6)
    return result

def roll2Dice():
    """ input: none
        output: number from 2-12
    """
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    roll = first + second
    return roll

def pickRPSMove():
    """Chooses a move from "rock", "paper", or "scissors" at random
    Input: None
    Returns: a string (see above)"""
    choices = ["rock", "paper", "scissors"]
    roll = random.randint(0, 2)
    return choices[roll]

def main():
    #with seed you can always get the same numbers...
    #without seed, it's based on the system clock
    #random.seed(1) 
    #One die, twice 
    for num in range(2):
        dieRoll = rollDie()
        print("1-6 roll is:", dieRoll)
    print("done")
    
    # Two dice, for dice games
    first = rollDie()
    second = rollDie()
    print("You rolled:", first, second)
    result = roll2Dice()
    print("2d6 roll:", result)

    # Coin flip
    # try one - 0 is heads, 1 is tails
    sides = ['Heads', 'Tails']
    print("Coin flip:")
    for flip in range(2):
        coinFlip = random.randint(0, 1)
        print( sides[coinFlip] )

    # Rock paper scissors - we'll make this a function
    print("RPS:")
    for hand in range(3):
        myHand = pickRPSMove()
        yourHand = pickRPSMove()
        print("I picked", myHand, "and you picked", yourHand)
        
    



# start program
main()
