# CTI 110
# P5LAB3 - Game Demo
# Name
# Date

# Uses code from P5T3


import random


def pickRPSMove():
    """Chooses a move from "rock", "paper", or "scissors" at random
    Input: None
    Returns: a string (see above)"""
    choices = ["rock", "paper", "scissors"]
    roll = random.randint(0, 2)
    return choices[roll]

def playerChoosesMove():
    """returns "rock" "paper" or "scissors" depending on player choice."""
    repeat = True
    while repeat:
        choice = input("Choose (rock/paper/scissors): ")
        choice = choice.lower() # remove capitals
        if choice == "rock" or choice == "paper" or choice == "scissors":
            repeat = False # we got a good choice
        else:
            print("That's not a valid choice.")
    return choice 

def PlayOneRound():
    """Play one round of RPS.
    Input: None
    Output: returns "player" or "cpu", depending on who won
    """
    winner = None # hold the winner's name (or None if tie)
    
    # ask user to pick a move
    playerMove = playerChoosesMove()
    # CPU picks a move at random
    cpuMove = pickRPSMove()
    # compare to see who wins
    print("You picked", playerMove, ",CPU picked", cpuMove)
    if playerMove == "rock":
        if cpuMove == "rock":       # tie, nobody wins
            pass                    
        if cpuMove == "scissors":   # R beats S
            winner = "player"   
        if cpuMove == "paper":      # P beats R
            winner = "cpu"

    if playerMove == "paper":
        if cpuMove == "rock":
            winner = "player"       # P beats R        
        if cpuMove == "scissors":   
            winner = "cpu"          # S beats P
        if cpuMove == "paper":      
            pass                    # tie, nobody wins
        
    if playerMove == "scissors":
        if cpuMove == "rock":
            winner = "cpu"          # R beats S       
        if cpuMove == "scissors":   
            pass                    # tie
        if cpuMove == "paper":      
            winner = "player"       # S beats P
    
    # announce winner
    return winner

def main():
    keepGoing = "y"
    while keepGoing == "y":
        winner = PlayOneRound()
        print(winner, "won that round.")
        keepGoing = input("again? (y/n): ")
    
# start program
main()
