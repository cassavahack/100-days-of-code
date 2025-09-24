from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# latte = MenuItem(name="latte",
#                  cost=1.5,
#                ingredients={
#     "water": 200,
#     "milk": 150,
#     "coffee": 24},
# )


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order_name = input(f"What would you like to drink? ({menu.get_items()}): ")

    drink = menu.find_drink(order_name)
    if not drink:
        order_name = input(f"What would you like to drink? ({menu.get_items()}): ")



    order = coffee_maker.is_resource_sufficient(drink)



    if order:
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)








