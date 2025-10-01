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

coffee_maker.make_coffee(latte)


# #while True:
#     options = menu.get_items()
#     order_name = input(f"what would you like to drink{options}").lower()
#
#     if order_name == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(order_name)
#
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
#




