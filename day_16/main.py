from day_16.menu import Menu
from day_16.coffee_maker import CoffeeMaker
from day_16.money_machine import MoneyMachine

input_drink = Menu()
checked = CoffeeMaker()
checked_money = MoneyMachine()

go_next = True

# while go_next:
#     choice_person = input(f"What would you like? {input_drink.get_items()}: ")
#     if choice_person == "off":
#         go_next = False
#     elif choice_person == "report":
#         checked.report()
#         checked_money.report()
#     elif choice_person == "espresso":
#         choice_person = input_drink.find_drink("espresso")
#         if checked.is_resource_sufficient(choice_person):
#             if checked_money.make_payment(1.5):
#                 checked.make_coffee(choice_person)
#     elif choice_person == "latte":
#         choice_person = input_drink.find_drink("latte")
#         if checked.is_resource_sufficient(choice_person):
#             if checked_money.make_payment(2.5):
#                 checked.make_coffee(choice_person)
#     elif choice_person == "cappuccino":
#         choice_person = input_drink.find_drink("cappuccino")
#         if checked.is_resource_sufficient(choice_person):
#             if checked_money.make_payment(3):
#                 checked.make_coffee(choice_person)

while go_next:
    choice_person = input(f"What would you like? {input_drink.get_items()}: ")
    if choice_person == "off":
        go_next = False
    elif choice_person == "report":
        checked.report()
        checked_money.report()
    else:
        drink = input_drink.find_drink(choice_person)

        if checked.is_resource_sufficient(drink) and checked_money.make_payment(drink.cost):
            checked.make_coffee(drink)
