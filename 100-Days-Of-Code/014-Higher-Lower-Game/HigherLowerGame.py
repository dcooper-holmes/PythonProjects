
import random
import os
from game_data import data
from art import *

# This accesses the dictionary and prints the value of 'follower_count'
# print(data[0]['follower_count'])

def checkAnswer(compare_a, compare_b, userChoice):
    '''This function compares the follower count of A and B to determine which is higher and then checks whether the users choice is equal to the correct answer.
    If it is it will return True else it will return False.'''

    if compare_a['follower_count'] > compare_b['follower_count']:
        correctAnswer = "a"
    elif compare_a['follower_count'] < compare_b['follower_count']:
        correctAnswer = "b"

    if userChoice == correctAnswer:
        return True

def higherlower():
    '''This is the function which runs the Higher or Lower game.'''

    score = 0

    compare_a = random.choice(data)
    compare_b = random.choice(data)

    wrongAnswer = False
    
    print(logo)

    while not wrongAnswer:

        compare_a = compare_b
        compare_b = random.choice(data)

        # print(f"DEBUG: Compare A: {compare_a['name']} / {compare_a['follower_count']}")
        print(f"Compare A: {compare_a['name']}")

        print(vs + "\n")

        # print(f"DEBUG: Compare B: {compare_b['name']} / {compare_b['follower_count']}")
        print(f"Against B: {compare_b['name']}")

        userChoice = input("Who has the most followers?: ").lower()

        answer = checkAnswer(compare_a, compare_b, userChoice)

        if answer:
            os.system('cls')
            print("Correct!")
            score += 1
        else:
            os.system('cls')
            print(logo)
            print(f"Incorrect! Game Over. Your score is: {str(score)}")
            wrongAnswer = True


higherlower()