from day_12.art import logo
import random

numbers_guessing = random.randint(1, 100)


def f_choose_difficulty():
    # This is function select difficulty
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {numbers_guessing}")
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_difficulty == "easy":
        choose_difficulty = 10
    else:
        choose_difficulty = 5
    return choose_difficulty


def guess(guess_number, difficult):
    # The basic logic behind this function is that we guess the number in the loop.
    # The function will terminate if the try counter runs out or the player guesses the number.
    if difficult == 10:
        counter = 10
    else:
        counter = 5
    print(f"You have {difficult} attempts remaining to guess the number.")
    go_guess = True
    while go_guess:
        counter -= 1
        make_guess = int(input("Make a guess: "))
        if make_guess == guess_number:
            print(f"You got it! The answer was {make_guess}.")
            go_guess = False
        elif make_guess > guess_number:
            if counter == 0:
                print("Too high.\nYou've run out of guesses, you lose.")
                go_guess = False
            else:
                print(f"Too high.\nGuess again\nYou have {counter} attempts remaining to guess the number.")
        elif make_guess < guess_number:
            if counter == 0:
                print("Too low.\nYou've run out of guesses, you lose.")
                go_guess = False
            else:
                print(f"Too low.\nGuess again\nYou have {counter} attempts remaining to guess the number.")


guess(numbers_guessing, f_choose_difficulty())

go_next = True
while go_next:
    want_more = input("Would you like to play more? Type 'y' or 'n': ")
    numbers_guessing = random.randint(1, 100)
    if want_more == "y":
        guess(numbers_guessing, f_choose_difficulty())
    else:
        go_next = False
