
tasks = []

def main():

    running = True

    while running:
        
        print("[Please select from the following options]")
        print("1 = View Tasks | 2 = Add Task | 3 = Remove Task | 4 = Quit")
        
        selection = input("")

        if selection == "1":
            print("Option 1 selected")
            running = False

        elif selection == "2":
            print("Option 2 selected")
            running = False

        elif selection == "3":
            print("Option 3 selected")
            running = False

        elif selection == "4":
            print("Option 4 selected")
            running = False

main()