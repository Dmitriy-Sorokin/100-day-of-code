import random

random_user = int(input("Hi please word 1, 2, 3, when 1-rock, 2-paper, 3-scissor: "))

random_comp = random.randint(1, 3)

rps_comp = ["rock", "paper", "scissor"]
rps_user = ["rock", "paper", "scissor"]

choice_copm = rps_comp[random_comp - 1]
choice_user = rps_user[random_user - 1]

if choice_copm == "rock" and choice_user == "rock":
    print("Computer chose: rock\nYou chose: rock\nIt's a draw")
elif choice_copm == "rock" and choice_user == "paper":
    print("Computer chose: rock\nYou chose: paper\nUser WIN!!!!")
elif choice_copm == "rock" and choice_user == "scissor":
    print("Computer chose: rock\nYou chose: scissor\nUser LOSE<(-_-)>")
elif choice_copm == "paper" and choice_user == "rock":
    print("Computer chose: paper\nYou chose: rock\nUser LOSE<(-_-)>")
elif choice_copm == "paper" and choice_user == "paper":
    print("Computer chose: paper\nYou chose: paper\nIt's a draw")
elif choice_copm == "paper" and choice_user == "scissor":
    print("Computer chose: paper\nYou chose: scissor\nUser WIN!!!!")
elif choice_copm == "scissor" and choice_user == "rock":
    print("Computer chose: scissor\nYou chose: rock\nUser WIN!!!!")
elif choice_copm == "scissor" and choice_user == "paper":
    print("Computer chose: scissor\nYou chose: paper\nUser LOSE<(-_-)>")
elif choice_copm == "scissor" and choice_user == "scissor":
    print("Computer chose: scissor\nYou chose: scissor\nIt's a draw")
