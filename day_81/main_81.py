from dact_morse import morze

next_step = True

while next_step:
    player_inp = input("Write word: ")

    list_morse = [morze[i] for i in player_inp if i in morze]
    print(list_morse)
    another_word = input("If you still want to code the word write (yes) if you don't want to write (no): ").lower()
    if another_word == "yes":
        pass
    else:
        next_step = False
