from functions import *

def main():

    tasks = []

    running = True

    while running:
        
        print("[Please select from the following options]")
        print("1 = View Tasks | 2 = Add Task | 3 = Remove Task | 4 = Quit")
        
        selection = input("\nOption: ")

        if selection == "1":
            view_tasks(tasks)

        elif selection == "2":
            tasks.append(create_task())

        elif selection == "3":
            print("Option 3 selected")
            running = False

        elif selection == "4":
            print("\nGoodbye.")
            running = False

main()