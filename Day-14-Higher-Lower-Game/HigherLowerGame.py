
import random
from game_data import data
from art import *

# This accesses the dictionary and prints the value of 'follower_count'
# print(data[0]['follower_count'])

def higherlower():

    wrongAnswer = False
    
    print(logo)

    compare_a = random.choice(data)
    compare_b = random.choice(data)

    while not wrongAnswer:

        print(f"Compare A: {compare_a['name']}")

        print(vs + "\n")

        print(f"Against B: {compare_b['name']}")

        user_choice = input("Who has the most followers?: ").lower()

        compare_a = compare_b
        compare_b = random.choice(data)


higherlower()