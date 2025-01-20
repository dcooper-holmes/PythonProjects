from functions import task, create_task

def main():

    tasks = []

    running = True

    while running:
        
        print("[Please select from the following options]")
        print("1 = View Tasks | 2 = Add Task | 3 = Remove Task | 4 = Quit")
        
        selection = input("")

        if selection == "1":
            print("Option 1 selected")
            running = False

        elif selection == "2":
            tasks.append(create_task())

        elif selection == "3":
            print("Option 3 selected")
            running = False

        elif selection == "4":
            print("Option 4 selected")
            running = False

main()