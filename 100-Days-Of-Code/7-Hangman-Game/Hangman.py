import random
import os
from Hangman_art import stages
from Hangman_art import logo
from Hangman_words import word_list

stages = stages

lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
game_over = False

print(logo + "\n")

#For Debugging Purposes
print(f"Pssstt.. The chosen word is: {chosen_word}\n")

display = []

word_length = len(chosen_word)

for letter in range(word_length):
    display.append("_")

while game_over == False:

    print(display)

    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess not in chosen_word:
        if lives > 1:
            lives -= 1
            print(stages[lives])
        else:
            print(stages[lives - 1])
            print("Game Over")
            game_over = True
    else:
        print(stages[lives])

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if "_" not in display:
        game_over = True
        print(f"You Win! The word was: {chosen_word}")