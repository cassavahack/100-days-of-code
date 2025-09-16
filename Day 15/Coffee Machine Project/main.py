MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 300,

}
from decimal import Decimal
import time

def is_resource_sufficient(drink_name):
    recipe = MENU[drink_name]["ingredients"]

    # Check each required ingredient against available resources
    for item, amt_needed in recipe.items():
        if resources[item] < amt_needed:
            print(f"Sorry, there is not enough {item}.")
            return False, item  # not enough of this ingredient

    # If loop completes, all resources are available
    return True, None


def check_resources():
    for key, value in resources.items():
        print(f"{key}:{value}")




def process_coins():
    q = int(input("how many quarters?: "))*25
    d = int(input("how many dimes?: "))*10
    n = int(input("how many nickles?: "))*5
    p = int(input("how many pennies?: "))*1
    total = q+d+n+p
    return total


def transaction_check(amount_paid,drink_cost):
    if amount_paid < drink_cost:
        print("Sorry not enough money")
        return False,0
    elif amount_paid >= drink_cost:
        change = amount_paid - drink_cost
        if change > 0:
            print(f"here is your change {change}")
        return True, change






def make_drink(drink_name):
    recipe = MENU[drink_name]["ingredients"]
    price = MENU[drink_name]["cost"]
    for item, amt in recipe.items():
        resources[item] -= amt

    resources["money"] += price

    print(f"Here is your {drink_name}. Enjoy!")








#TODO:1 prompt user by asking what they want.
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if choice == "off":
        print("CoffeeMachine: Stopping services...")
        time.sleep(0.6)
        print("CoffeeMachine: Shutdown complete. ☕️ Goodbye.")
        break

    if choice == "report":
        check_resources()
        continue

    # Validate drink choice
    if choice not in MENU:
        print("Sorry, that is not on the menu.")
        continue

    # 1) Check resources
    ok, missing = is_resource_sufficient(choice)
    if not ok:
        # Message already printed inside is_resource_sufficient
        continue

    # 2) Take coins
    total_paid = process_coins()

    # 3) Transaction decision
    price = MENU[choice]["cost"]           # in cents
    approved, change = transaction_check(total_paid, price)
    if not approved:
        # not enough money, refund implied
        continue

    # 4) Make the drink
    make_drink(choice)

#TODO:2 Turn off the coffee machine entering off


#TODO:3 Print report which takes inventory of resources


#TODO:4 Check for suffcient resources
#TODO:5 Process coins
#TODO:6 Check if transactiosn are succesful
#TODO:7 Make coffee



