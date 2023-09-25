import os

def newPet() :
    
    #Making Pets directory
    os.mkdir("./Pets")

    #For Debugging
    print("LOG: Pets directory created...\n")
    #//


    #Pet Name
    happy_with_name = False

    while happy_with_name == False:

        pet_name = input("What would you like to call your pet? ")
        os.system('cls')

        user_input = input("Your pet's name is: " + pet_name + ". Is that correct? Y = yes / N = no\n")

        if user_input == "Y" or user_input == "y":
            happy_with_name = True
        else:
            os.system('cls')
            happy_with_name = False