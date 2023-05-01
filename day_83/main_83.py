from day_83.checker import checker_win


def board_example():
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')




def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]}  ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]}  ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]}  ')




def logic_game():
    print("Example board. In lead a number to select a location: ")
    board_example()
    board_user = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    next_step = False
    while not next_step:
        try:
            while True:
                choose_user_1 = int(input("On the example board, look at where you want to put the cross and enter that number player word(X): "))
                if board_user[choose_user_1 - 1] == " ":
                    board_user[choose_user_1 - 1] = "X"
                    break
                else:
                    print("Choose different place")
        except ValueError:
            print("Only number example board 1-9")
            continue
        except IndexError:
            print("Only number example board 1-9")
            continue
        print("Games board")

        print_board(board=board_user)
        next_step = checker_win(board=board_user)
        if next_step:
            while True:
                more = input("Do you want more game? yes or no: ").lower()
                if more == "yes":
                    logic_game()
                elif more == "no":
                    print("See you later")
                    break
                else:
                    print("Pleas write correctly word!!!")

        while True:
            try:
                choose_user_2 = int(input("On the example board, look at where you want to put the cross and enter that number player word(0): "))
                if board_user[choose_user_2 - 1] == " ":
                    board_user[choose_user_2 - 1] = "0"
                    break
                else:
                    print("Choose different place")
            except ValueError:
                print("Only number example board 1-9")
                continue
            except IndexError:
                print("Only number example board 1-9")
                continue

        print("Games board")
        print_board(board=board_user)
        next_step = checker_win(board=board_user)
        if next_step:
            while True:
                more = input("Do you want more game? yes or no: ").lower()
                if more == "yes":
                    logic_game()
                elif more == "no":
                    print("See you later")
                    break
                else:
                    print("Pleas write correctly word!!!")

logic_game()