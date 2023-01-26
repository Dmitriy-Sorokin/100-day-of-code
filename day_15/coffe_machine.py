from day_15.data import *


# 1. Print report


def person_choice_coffee():
    global choices_coffee
    global go_next
    choices_coffee = "espresso"  # input("What would you like? (espresso/latte/cappuccino): ")
    if choices_coffee == "report":
        print(
            f"Water: {resources['water']}\n"
            f"Milk: {resources['milk']}\n"
            f"Coffee: {resources['coffee']}\n"
            f"Money: $0"
        )
    elif choices_coffee == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["espresso"]["ingredients"]["coffee"]:
            print(123124214)
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
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        return choices_coffee
    elif choices_coffee == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        return choices_coffee
    else:
        return choices_coffee


# print(person_choice_coffee())
# print(resources)

def counting_money():
    counter_money = 0
    inp_quarters = 20  # int(input("how many quarters?: "))
    inp_dimes = 3  # int(input("how many dimes?: "))
    inp_nickles = 2  # int(input("how many nickles?: "))
    inp_pennies = 1  # int(input("how many pennies?:"))
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
        print(f"Here is your {choice_coffee} ☕️. Enjoy!")
    elif choice_coffee == "latte":
        money -= MENU["latte"]["cost"]
        print(f"Here is ${money} in change.")
        print(f"Here is your {choice_coffee} ☕️. Enjoy!")
    elif choice_coffee == "cappuccino":
        money -= MENU["cappuccino"]["cost"]
        print(f"Here is ${money} in change.")
        print(f"Here is your {choice_coffee} ☕️. Enjoy!")


# print(person_choice_coffee())
# print(person_choice_coffee())
# print(person_choice_coffee())
# print(person_choice_coffee())
# print(person_choice_coffee)

go_next = True
while go_next:
    if person_choice_coffee():
        if choices_coffee == "report":
            pass
        if choices_coffee == "off":
            print("pfgecnbkf")
            go_next = False
        final_input(choice_coffee=choices_coffee, money=counting_money())

    # if person_choice_coffee() == False:
    #     go_next = False
# elif counting_money() is None:
#     go_next = False
# # else:
# person_choice_coffee()
# counting_money()
# choice_coffee_person(person_choice_coffee(), counting_money())

# 3. Proces  coin

# 4. Check transaction sucsesful?

# 5. Make coffe
