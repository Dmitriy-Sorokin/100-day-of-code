from day_15.data import *


def person_choice_coffee():
    global choices_coffee
    global go_next
    choices_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if choices_coffee == "report":
        print(
            f"Water: {resources['water']}\n"
            f"Milk: {resources['milk']}\n"
            f"Coffee: {resources['coffee']}\n"
            f"Money: $0"
        )
    elif choices_coffee == "off":
        go_next = False
        return go_next
    elif choices_coffee == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["espresso"]["ingredients"]["coffee"]:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Выбрал эспрессо")
            return choices_coffee
        elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            go_next = False
            return go_next
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            go_next = False
            return go_next
    elif choices_coffee == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and \
                resources["milk"] >= MENU["latte"]["ingredients"]["milk"] \
                and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            print("выбрал лате")
            return choices_coffee
        elif resources["water"] <= MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            go_next = False
            return go_next
        elif resources["milk"] < MENU["espresso"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            go_next = False
            return go_next
        elif resources["coffee"] <= MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            go_next = False
            return go_next
    elif choices_coffee == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and \
                resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and \
                resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            print("выбрал капыч")
            return choices_coffee
        elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            go_next = False
            return go_next
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            go_next = False
            return go_next
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            go_next = False
            return go_next


def counting_money():
    counter_money = 0
    inp_quarters = int(input("how many quarters?: "))
    inp_dimes = int(input("how many dimes?: "))
    inp_nickles = int(input("how many nickles?: "))
    inp_pennies = int(input("how many pennies?:"))
    counter_money += (coins["quarters"] * inp_quarters)
    counter_money += (coins["dimes"] * inp_dimes)
    counter_money += (coins["nickles"] * inp_nickles)
    counter_money += (coins["pennies"] * inp_pennies)
    total_money = round(counter_money, 2)
    if total_money < 3:
        print("Sorry that's not enough money. Money refunded.")
    else:
        return total_money


def final_input(choice_coffee, money):
    if choice_coffee == "espresso":
        money -= MENU["espresso"]["cost"]
        print(f"Here is ${money} in change.")
        print(f"Here is your {choice_coffee} ☕. Enjoy!")
    elif choice_coffee == "latte":
        money -= MENU["latte"]["cost"]
        print(f"Here is ${money} in change.")
        print(f"Here is your {choice_coffee} ☕. Enjoy!")
    elif choice_coffee == "cappuccino":
        money -= MENU["cappuccino"]["cost"]
        print(f"Here is ${money} in change.")
        print(f"Here is your {choice_coffee} ☕. Enjoy!")


go_next = True
while go_next:
    if person_choice_coffee():
        if choices_coffee == "report":
            pass
        if choices_coffee == "off":
            pass
        final_input(choice_coffee=choices_coffee, money=counting_money())
