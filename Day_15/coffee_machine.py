MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def turn_off():
    return False


def report():
    for key, value in resources.items():
        if key != "money":
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: ${value}0")


def check_resources(drink):
    enough = True
    for key, value in MENU.items():
        if key == drink:
            for k, v in value.items():
                if k == "ingredients":
                    for x, y in v.items():
                        if x in resources.keys():
                            if resources[x] >= y:
                                pass
                            elif resources[x] < y:
                                print(f"Sorry, there is not enough {x}")
                                enough = False
    return enough


def process_coins(drink):
    """
    Takes the drink the user input and displays the price. User is then prompted to pay using quarters, dimes,
    nickels and pennies. The function will calculate the total entered by the user to determine if it is enough to
    cover the cost of the drink
    :param drink:
    :return: price, total_entered
    """
    price = round((MENU[drink]["cost"]), 2)
    print(f"Price: ${price}")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_entered = round(((quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)), 2)
    return price, total_entered


def log_transaction(price, total):
    transaction = True
    if total >= price:
        change = round((total - price), 2)
        print(f"Here is ${change} in change")
        if "money" in resources:
            resources["money"] += price
        else:
            resources["money"] = price
    else:
        print("Sorry, that's not enough money. Money refunded.")
        transaction = False
    return transaction


def update_resources(drink):
    for key, value in MENU[drink]["ingredients"].items():
        resources[key] -= value
    return 0


machine_on = True

while machine_on:
    user_prompt = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_prompt == "off":
        machine_on = turn_off()
    elif user_prompt == "report":
        report()

    elif user_prompt == "espresso" or user_prompt == "latte" or user_prompt == "cappuccino":
        if check_resources(user_prompt):
            drink_price, cust_total = process_coins(user_prompt)
            print(f"You gave me: ${cust_total}")
            # log_transaction(drink_price, cust_total)
            if log_transaction(drink_price, cust_total):
                update_resources(user_prompt)
                print(f"Here is your {user_prompt} ☕. Enjoy!")