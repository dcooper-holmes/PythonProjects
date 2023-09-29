import os
import art

art

no_more_bidders = False

bids = {}

def find_highest_bidder(bids):

    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    os.system('cls')
    print(f"The winner is {winner} with a bid of £{highest_bid}")

while not no_more_bidders:

    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))

    bids[name] = bid

    if input("Are there any more bidders? Yes / No : ").lower() == "no":
        no_more_bidders = True
        find_highest_bidder(bids)

    else:
        os.system('cls')

