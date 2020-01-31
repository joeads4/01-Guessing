import sys
import random

assert sys.version_info >= (3, 7), "This script requires at least Python 3.7"

guessTotal = 0
answer = random.randint(0, 50)
playerGuess = input("Choose a number between 1 and 50.\n")

while playerGuess != answer:
    while not isinstance(playerGuess, int):
        try:
            playerGuess = int(playerGuess)
        except ValueError:
            print("Invalid entry.")
            playerGuess = input("Choose a number between 1 and 50.\n")

    if playerGuess < answer and playerGuess > 0:
        print("Your guess is too low.")
        guessTotal += 1
        playerGuess = input("Choose a number between 1 and 50.\n")
    elif playerGuess > answer and playerGuess < 51:
        print("Your guess is too high.")
        guessTotal += 1
        playerGuess = input("Choose a number between 1 and 50.\n")
    elif playerGuess > 50:
        print("That number is out of range.")
        guessTotal += 1
        playerGuess = input("Choose a number between 1 and 50.\n")
    elif playerGuess <= 0:
        print("That number is out of range.")
        guessTotal += 1
        playerGuess = input("Choose a number between 1 and 50.\n")
    else:
        print("Correct!\nYour total number of guesses was: " + str(guessTotal))
