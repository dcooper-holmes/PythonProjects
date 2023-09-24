import os
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

newList = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")

#User Selection
userChoice = int(input("Choose '1' for Rock, '2' for Paper & '3' for Scissors\n")) - 1

#Computer Selection
computerChoice = random.randint(1, 3) - 1

#Selection Text
userOutcome = ""
computerOutcome = ""

if str(userChoice) == "0":
    userOutcome = "You have chosen Rock!\n"
elif  str(userChoice) == "1":
    userOutcome = "You have chosen Paper!\n"
elif str(userChoice) == "2":
    userOutcome = "You have chosen Scissors!\n"

if str(computerChoice) == "0":
    computerOutcome = "The computer has chosen Rock!\n"
elif  str(computerChoice) == "1":
    computerOutcome = "The computer has chosen Paper!\n"
elif str(computerChoice) == "2":
    computerOutcome = "The computer has chosen Scissors!\n"

#Results
result = ""

if userChoice >= 3 or userChoice < 0: 
  result = "You typed an invalid number, you lose!"
elif userChoice == 0 and computerChoice == 2:
    result = "You Win!"
elif computerChoice == 0 and userChoice == 2:
    result = "You Lose!"
elif computerChoice > userChoice:
    result = "You Lose!"
elif userChoice > computerChoice:
    result = "You Win!"
elif userChoice == computerChoice:
    result = "Its a draw!"

os.system('cls')
print(userOutcome + newList[userChoice] + "\n")

print(computerOutcome + newList[computerChoice] + "\n")

print(result)


