from day_83.checker import checker_win


def board_example():
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')


board_user = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]}  ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]}  ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]}  ')

print("Example board. In lead a number to select a location: ")
board_example()

next_step = False
while not next_step:
    try:
        choose_user_1 = int(input("On the example board, look at where you want to put the cross and enter that number player word(X): "))
    except ValueError:
        print("Only number example board 1-9")
        continue
    print("Games board")
    board_user[choose_user_1 - 1] = "X"
    print_board(board=board_user)
    next_step = checker_win(board=board_user)
    if next_step:
        break
    try:
        choose_user_2 = int(input("On the example board, look at where you want to put the cross and enter that number player word(0): "))
    except ValueError:
        print("Only number example board 1-9")
        continue
    print("Games board")
    board_user[choose_user_2 - 1] = "0"
    print_board(board=board_user)
    checker_win(board=board_user)

