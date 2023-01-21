import random
from day_11.logo import logo


go_next = True
while go_next:
    play_some_more = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_some_more == "n":
        go_next = False
    else:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        print(logo)

        next_play = ""
        player_card = []


        def player():
            if next_play == "y":
                random_card_user = int(random.choice(cards))
                player_card.append(random_card_user)
            else:
                for _ in range(1, 3):
                    random_card_user = int(random.choice(cards))
                    player_card.append(random_card_user)
            return player_card


        comp_first_card = []


        def computer():
            if next_play == "y" or next_play == "n":
                while not int(sum(comp_first_card)) >= 17:
                    random_card_comp = int(random.choice(cards))
                    comp_first_card.append(random_card_comp)
            else:
                random_card_comp = int(random.choice(cards))
                comp_first_card.append(random_card_comp)
            return comp_first_card


        print(f" Your cards: {player()}, current score: {sum(player_card)} ")
        computer()
        print(f"Computer's first card: {comp_first_card[0]}")

        go = True
        while go:
            next_play = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_play == "y":
                print(f" Your cards: {player()}, current score: {sum(player_card)} ")
                print(f"Computer's first card: {comp_first_card[0]}")
            if sum(player_card) > 21:
                go = False
            else:
                go = False

        computer()
        print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
        print(f"Computer's final hand: {comp_first_card}, final score: {sum(comp_first_card)}")

        if sum(player_card) > 21:
            print("You went over. You lose")
        elif sum(comp_first_card) > 21:
            print("Opponent went over. You win!")
        elif sum(player_card) < sum(comp_first_card):
            print("You loose")
        elif sum(player_card) == sum(comp_first_card):
            print(f"Broken")
        else:
            print(f"You win!")


