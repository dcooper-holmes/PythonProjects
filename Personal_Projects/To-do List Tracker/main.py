import os
import time
from functions import *

def main():

    tasks = []

    running = True

    while running:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("[Please select from the following options]")
        print("1 = View Tasks | 2 = Add Task | 3 = Remove Task | 4 = Quit")
        
        selection = input("\nOption: ")

        if selection == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(tasks) > 0:
                view_tasks(tasks)
                input("Press any key to go back to the menu...")
            else:
                print("You have no tasks available to view...\nReturning to Main Menu...")
                time.sleep(2)

        elif selection == "2":

            creating_tasks = True

            while creating_tasks:

                os.system('cls' if os.name == 'nt' else 'clear')

                tasks.append(create_task(tasks))

                if input("\nWould you like to create another task? Y/N: ").lower() == "y":
                    creating_tasks = True
                else:
                    creating_tasks = False

        elif selection == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(tasks) > 0:
                delete_task(tasks)
            else:
                print("You have no tasks available which you can delete...\nReturning to Main Menu...")
                time.sleep(2)

        elif selection == "4":
            print("\nGoodbye.")
            running = False

main()