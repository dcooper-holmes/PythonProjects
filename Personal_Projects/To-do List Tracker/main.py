import os
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

            view_tasks(tasks)

        elif selection == "2":

            creating_tasks = True

            while creating_tasks:

                os.system('cls' if os.name == 'nt' else 'clear')

                tasks.append(create_task())

                if input("\nWould you like to create another task? Y/N: ").lower() == "y":
                    creating_tasks = True
                else:
                    creating_tasks = False

        elif selection == "3":
            print("Option 3 selected")
            running = False

        elif selection == "4":
            print("\nGoodbye.")
            running = False

main()