from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

on = True

while on:

    selection = input(f'What would you like? ({menu.get_items()}): ')

    if selection.lower() == "off":
        on = False

    elif selection.lower() == "report":
        print(coffee.report())
        print(money.report())

    elif menu.find_drink(selection):
        drink = menu.find_drink(selection)

        canMake = coffee.is_resource_sufficient(drink)

        if canMake:

            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
