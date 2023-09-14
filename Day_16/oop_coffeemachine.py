from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
my_coffee = CoffeeMaker()
my_menu = Menu()
coin_machine = MoneyMachine()

while machine_on:
    user_prompt = input(f"\nWhat would you like? ({my_menu.get_items()}): ").lower()
    if user_prompt == "off":
        machine_on = False
    elif user_prompt == "report":
        my_coffee.report()
        coin_machine.report()
    else:
        drink = my_menu.find_drink(user_prompt)
        if my_coffee.is_resource_sufficient(drink):
            print(f"Price: {drink.cost}")
            if coin_machine.make_payment(drink.cost):
                my_coffee.make_coffee(drink)
