from day_14.art import *
from day_14.game_data import data
import random
import os

random_person1 = []


def person1(rand_p1):
    rand_int_p1 = random.randint(0, 49)
    r_person1 = data[rand_int_p1]
    rand_p1.clear()
    rand_p1.append(r_person1)


random_person2 = []


def person2(rand_p2):
    rand_int_p2 = random.randint(0, 49)
    r_person2 = data[rand_int_p2]
    rand_p2.clear()
    rand_p2.append(r_person2)


person1(rand_p1=random_person1)
person2(rand_p2=random_person2)


def choice_player():
    print(logo)
    print(
        f"Compare A: {random_person1[0]['name']}, a {random_person1[0]['description']}, from {random_person1[0]['country']}.")
    print(vs)
    print(
        f"Compare B: {random_person2[0]['name']}, a {random_person2[0]['description']}, from {random_person2[0]['country']}.")
    go_next = True
    counter = 0
    while go_next:
        counter += 1
        player_select = input("Who has more followers? Type 'A' or 'B': ")
        if player_select == "a":
            if random_person1[0]['follower_count'] >= random_person2[0]['follower_count']:
                os.system("cls")
                print(logo)
                print(f"You're right! Current score: {counter}.")
                print(
                    f"Compare A: {random_person1[0]['name']}, a {random_person1[0]['description']}, from {random_person1[0]['country']}.")
                print(vs)
                person2(rand_p2=random_person2)
                print(
                    f"Compare B: {random_person2[0]['name']}, a {random_person2[0]['description']}, from {random_person2[0]['country']}.")
            else:
                os.system("cls")
                print(logo)
                print(f"Sorry, that's wrong. Final score: {counter}")
                go_next = False
        elif player_select == "b":
            if random_person2[0]['follower_count'] >= random_person1[0]['follower_count']:
                os.system("cls")
                print(logo)
                print(f"You're right! Current score: {counter}.")
                print(
                    f"Compare A: {random_person2[0]['name']}, a {random_person2[0]['description']}, from {random_person2[0]['country']}.")
                print(vs)
                person1(rand_p1=random_person1)
                print(
                    f"Compare B: {random_person1[0]['name']}, a {random_person1[0]['description']}, from {random_person1[0]['country']}.")
            else:
                os.system("cls")
                print(logo)
                print(f"Sorry, that's wrong. Final score: {counter}")
                go_next = False


choice_player()
