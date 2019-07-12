# Program that guess number in the range of 1 to 100
# July 12 2019
# CTI-110 P5HW1 - Random Number
# Freddy Ojeda

import random

# Generating a random number
r = random.randint(1,100)

# Variable to track the number of attempts
attempts=0
# looping
while True:
    # Getting the user guess
    n = input("\nEnter your guess (1 to 100)(enter to quit): ")

    # Incrementing the counter
    attempts+=1

    # Checking for n
    if n:

        # Converting string to int
        n=int(n)

        # Checking for guess number equal to random number
        if r == n:
          
            print("\nCongratulations! You have guessed the number.")
            print("Number of attempts= ",attempts)

        # Checking for guess number greater than random number
        elif n > r:
            print("\nToo high, try again.")
          
        # Checking for guess number lower than random number
        elif n < r:
            print("\nToo low, try again.")
          
    else:
        break
