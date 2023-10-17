import os
import random
from art import logo

EASY_GUESSES = 10
HARD_GUESSES = 5

def chooseDifficulty():
    """This function returns the number of guesses based off of the users input: 'easy' = 10 / 'hard' = 5."""

    userInput = input("\nChoose a difficulty. Type 'Easy' or 'Hard': ").lower()
    if userInput == "easy":
        return EASY_GUESSES
    elif userInput == "hard":
        return HARD_GUESSES
    else:
        game()

def checkAnswer(chosenNumber, userGuess):
    """This function takes the chosen number and compares it to the users guess. If the users guess is equal to the chosen number then the user wins and the game ends.
    \nIf the users guess is higher or lower then the chosen number then it will remove 1 from the number of guesses."""

    if userGuess > chosenNumber:
        print("Too High")
        return False
    elif userGuess < chosenNumber:
        print("Too Low")
        return False
    elif userGuess == chosenNumber:
        print(f"Correct! The number was {str(chosenNumber)}!")
        return True

def game():
    """This is the main function for the game."""

    chosenNumber = random.randint(1, 100)

    os.system('cls')
    print(logo)

    print("\nWelcome! I'm thinking of a number between 1 and 100")

    guesses = chooseDifficulty()

    os.system('cls')

    while guesses > 0:
        userGuess = input("Make a guess: ")

        isCorrect = checkAnswer(chosenNumber=chosenNumber, userGuess=int(userGuess))

        if not isCorrect:
            guesses -= 1
        else:
            guesses = 0

    if guesses == 0 and not isCorrect:
        print(f"\nYou have ran out of guesses. The number was {str(chosenNumber)}. You Lose.")

    if input("\nWould you like to play again? Type Y for Yes and N for No: ").lower() == "y":
        game()

game()