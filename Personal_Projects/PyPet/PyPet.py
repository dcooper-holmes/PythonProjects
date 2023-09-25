import os

from Functions.start import start
from Functions.newPet import newPet
from Functions.checkBalance import checkBalance

is_running = True

while is_running == True:
    os.system('cls')

    print("Welcome to PyPet! Your Virtual Desktop Python Pet!\n")

    print("Please select an option:\n")
    print("1 - Call your pet")
    print("2 - Check Balance")
    print("3 - Exit\n")

    selection = input("")

    if selection == "1":
        if start() == 1:
            os.system('cls')

            #For Debugging
            print("LOG: start() has finished")
            #

    elif selection == "2":
        
        os.system('cls')
        print(checkBalance())

        #For Debugging
        print("LOG: checkBalance() has finished")
        #

    elif selection == "3":
        is_running = False