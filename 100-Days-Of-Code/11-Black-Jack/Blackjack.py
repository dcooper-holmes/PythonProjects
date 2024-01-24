import os
from art import logo
import random

def deal_card():
    """This function randomly chooses a card from the following list: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    random_card = random.choice(cards)

    return random_card

def calculate_score(cards):
    """This function takes a list of cards and calculates the sum."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_cards, computer_cards):
    """Compares the users score to the computers score and decides the winner unless it is a draw."""

    users_score = calculate_score(user_cards)
    computers_score = calculate_score(computer_cards)
    
    if users_score == computers_score:
        print(f"You have {users_score} and the computer has {computers_score}, It's a Draw!")

    elif computers_score == 0:
        print("The computer has Blackjack, You Lose.")

    elif users_score == 0:
        print("You have Blackjack! You Win!")

    elif users_score > 21:
        print(f"You have {users_score}, You are Bust.")

    elif computers_score > 21:
        print(f"The computer is bust with {computers_score}, You Win!")

    elif users_score > computers_score:
        print(f"You have {users_score}, the computer has {computers_score}, You Win!")

    elif users_score < computers_score:
        print(f"You have {users_score}, the computer has {computers_score}, You Lose.")

def blackjack():

    game_running = True

    while game_running:
        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]

        game_ended = False
        no_more_cards = False

        print(logo)

        while not game_ended:

            while not no_more_cards:
                os.system('cls')
                print(logo)
                if calculate_score(user_cards) < 21 and input(f"Your cards are {user_cards}, would you like another card? y = Yes / n = No: ").lower() == "y":
                    user_cards.append(deal_card())
                else:
                    os.system('cls')
                    print(logo)
                    while calculate_score(computer_cards) < 17:
                        computer_cards.append(deal_card())
                    no_more_cards = True
                    game_ended = True

        compare(user_cards, computer_cards)

        if input("Would you like to play another game? y = Yes / n = No: ").lower() == "y":
            os.system('cls')
        else:
            game_running = False

blackjack()