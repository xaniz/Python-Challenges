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
    "money:": 0,
}

next_coffee = True


while next_coffee:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "off":
        next_coffee = False
    elif coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money:']}")
    else:
        if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
            if MENU[coffee]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water.")
            elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk.")
            elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee.")
            else:
                print("Please insert coins")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
                inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
                if inserted < MENU[coffee]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] -= MENU[coffee]["ingredients"]["water"]
                    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
                    resources["money:"] += MENU[coffee]["cost"]
                    returning = round(inserted - MENU[coffee]["cost"], 2)
                    print(f"Here is your {coffee} ˗ˏˋ☕ˎˊ˗. Enjoy! The rest: {returning}")
        else:
            print("That type of coffee does not exist here")