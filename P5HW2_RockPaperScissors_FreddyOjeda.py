# Program that lets the user play the game of Rock, Paper, Scissors agains the computer.
# July 12 2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Freddy Ojeda

from random import randint

#Create a list of play options
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
computer = t[randint(0,2)]

#Set player to False
player = False

while player == False:
#Set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "wraps", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "wraps", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
# Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
