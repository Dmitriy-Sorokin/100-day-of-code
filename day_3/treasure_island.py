road = input("Welcome to Treasure Island.\n Your mission is to find the treasure.\nYou go left or right, L or R? ")
river = input("A boat should be arriving soon. But you can go afloat.\n Your swim or wait, S or W? ")
door = input(
    "Finally, you have one last choice before you. There are three doors in front of you.\nChoose the right one and get to the treasure!!!"
    "Red door, orange door or black door to choose from, R, O, B? ")

if road == "R" or road == "right":
    print("Unbelievable, you move on to adventure!!!")
    if river == "swim" or river == "S":
        print("Unbelievable, you move on to adventure!!!")
        if door == "black" or door == "B":
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
        else:
            print("Door not wrong you loos =(((")
    else:
        print("Game loos =((( Monsters ate into the boat <(-_-)>")
else:
    print("Games loos =(((")
