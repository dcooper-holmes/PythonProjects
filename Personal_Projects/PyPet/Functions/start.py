import os

def start():
    os.system('cls')

    if os.path.exists("./Pets") == False:

        #For Debugging
        print("LOG: Pets directory does not exist...")
        #//

        print("Hmm.. You don't appear to have a pet, would you like one? (The first ones free!)")
        
        selection = input("Type Y for Yes and N for No: ")

        if selection == "Y" or selection == "y":
            os.mkdir("./Pets")

            #For Debugging
            print("LOG: Pets directory created...")
            #//

    else:
        
        #For Debugging
        print("Pets directory exists...")
        print("Accessing pet...")
        input("Press enter to continue...")
        #//
        return(1)

    



