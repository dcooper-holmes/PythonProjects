
from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(selection):
    '''This function checks that the machine has sufficient resources to make the selected coffee.'''

    if selection == 'espresso':
        water_needed = MENU[selection]['ingredients']['water']
        milk_needed = 0
        coffee_needed = MENU[selection]['ingredients']['coffee']

    else:
        water_needed = MENU[selection]['ingredients']['water']
        milk_needed = MENU[selection]['ingredients']['milk']
        coffee_needed = MENU[selection]['ingredients']['coffee']

    if water_needed <= resources['water']:

        if milk_needed <= resources['milk']:

            if coffee_needed <= resources['coffee']:
                return True

            else:
                print("Insufficient Coffee")
                return False

        else:
            print("Insufficient Milk")
            return False

    else:
        print("Insufficient Water")
        return False


def make_transaction(selection):
    '''This function asks the user to enter coins and checks that the amount entered is sufficient for the selected coffee.'''

    money_entered = 0

    print("Please insert your coins...")

    quarters_entered = int(input("How many quarters: "))
    dimes_entered = int(input("How many dimes: "))
    nickles_entered = int(input("How many nickles: "))
    pennies_entered = int(input("How many pennies: "))

    money_entered = 0.25 * quarters_entered + 0.10 * dimes_entered + 0.05 * nickles_entered + 0.01 * pennies_entered

    if money_entered >= MENU[selection]['cost']:
        resources['money'] += money_entered
        return True
    else:
        return False


def make_drink(selection):
    '''This function makes the selected drink.'''

    if selection == 'espresso':
        water_needed = MENU[selection]['ingredients']['water']
        milk_needed = 0
        coffee_needed = MENU[selection]['ingredients']['coffee']

    else:
        water_needed = MENU[selection]['ingredients']['water']
        milk_needed = MENU[selection]['ingredients']['milk']
        coffee_needed = MENU[selection]['ingredients']['coffee']

    resources['water'] -= water_needed
    resources['milk'] -= milk_needed
    resources['coffee'] -= coffee_needed

    print(f"Making {selection}, Enjoy ☕!")


def coffee_machine():
    '''This is the main function which runs the Coffee machine.'''

    selection = input("What drink would you like? (espresso/latte/cappuccino): ")

    if selection == "off":
        return

    if selection == "report":
        print("Water: " + str(resources['water']))
        print("Milk: " + str(resources['milk']))
        print("Coffee: " + str(resources['coffee']))
        print("Money: " + str(resources['money']))
        coffee_machine()

    else:
        if check_resources(selection):

            if make_transaction(selection):

                make_drink(selection)

                if input("Would you like another drink? Y = yes / N = no: ").lower() == "y":
                    coffee_machine()

            else:
                print("Insufficient Coins, refunding money.")
                coffee_machine()

        else:
            coffee_machine()


coffee_machine()
