import os

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/        
*******************************************************************************''')

print("Welcome to Treasure Island!")
print("The treasure has been hidden somewhere on this island, find it an escape to win!\n")

#Choice 1
choice_1 = input("You come across a split in the path, would you like to go left or right? Type 'left' or 'right': ")

if choice_1 == "left":
    os.system('cls')

    #Choice 2
    choice_2 = input("You arrive at a river, do you swim across or do you wait for a boat? Type 'swim' or 'wait': ")

    if choice_2 == "wait":
        os.system('cls')

        #Choice 3
        choice_3 = input("You arrive at 3 doors, a red door, a blue door and a yellow door. Which door do you take? Type 'red', 'yellow' or 'blue': ")

        if choice_3 == "yellow":
            os.system('cls')
            print("Congratulations, you have found the treasure! You Win!")
        elif choice_3 == "blue":
            print("You are attacked by a snow monster! Game Over.")
        elif choice_3 == "red":
            print("You are sucked through the door into a black hole. Game Over.")
        else:
            os.system('cls')
            print("Game Over.")                                                         
    else:
        os.system('cls')
        print("You are attacked by a sea monster. Game Over.")
else:
    os.system('cls')
    print("You have fell into a hole full of Snakes. Game Over.")
    