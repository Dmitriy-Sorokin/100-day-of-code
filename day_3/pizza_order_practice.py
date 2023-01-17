# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size_s = 15
size_m = 20
size_l = 25
pep_small = 2
pep_medium_large = 3
cheez_y = 1

if size == "S":
    if add_pepperoni == "Y":
        print(f"Your final bill is: ${size_s + pep_small}.")
        if extra_cheese == "Y":
            print(f"Your final bill is: ${size_s + pep_small + cheez_y}.")
    elif extra_cheese == "Y":
        print(f"Your final bill is: ${size_s + cheez_y}.")
    else:
        print(f"Your final bill is: ${size_s}.")
elif size == "M":
    if add_pepperoni == "Y":
        print(f"Your final bill is: ${size_m + pep_medium_large}.")
        if extra_cheese == "Y":
            print(f"Your final bill is: ${size_m + pep_medium_large + cheez_y}.")
    elif extra_cheese == "Y":
        print(f"Your final bill is: ${size_m + cheez_y}.")
    else:
        print(f"Your final bill is: ${size_m}.")
elif size == "L":
    if add_pepperoni == "Y":
        print(f"Your final bill is: ${size_l + pep_medium_large}.")
        if extra_cheese == "Y":
            print(f"Your final bill is: ${size_l + pep_medium_large + cheez_y}.")
    elif extra_cheese == "Y":
        print(f"Your final bill is: ${size_l + cheez_y}.")
    else:
        print(f"Your final bill is: ${size_l}.")
