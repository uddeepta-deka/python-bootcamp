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

money_received = 0.0


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_value = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters
    return total_value


def are_enough_resources(item):
    required_resources = item["ingredients"]
    for ingredient in required_resources:
        if required_resources[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def make_order(item):
    required_resources = item["ingredients"]
    for ingredient in required_resources:
        resources[ingredient] -= required_resources[ingredient]
    return


def place_order():
    usr_order = input("What would you like?? (Espresso / latte / cappuccino): ").lower()
    available_items = ['espresso', 'latte', 'cappuccino']
    global money_received
    if usr_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_received}")
        place_order()

    elif usr_order in available_items:
        money_received += insert_coins()
        order_item = MENU[usr_order]

        if money_received < order_item["cost"]:
            print("Sorry that's not enough money. Money refunded")
            return
        elif are_enough_resources(order_item):
            make_order(order_item)
            money_received -= order_item["cost"]
            print(f"Here is ${money_received} in change. ")
            print(f"Here is your {usr_order}. Enjoy!")
            if input("Would you like to place another order? 'y' or 'n': ") == 'y':
                place_order()
            else:
                return
        else:
            print(f"Here is ${money_received} for refund.")
            return
    else:
        print("Sorry, invalid order. Please try again")
        place_order()


place_order()
