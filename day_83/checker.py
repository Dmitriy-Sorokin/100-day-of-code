def checker_win(board):
    if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "0":
        print(f"Player {board[0]}  WIN!!!!")
        return True
    elif board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "0":
        print(f"Player {board[3]} WIN!!!!")
        return True
    elif board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "0":
        print(f"Player {board[6]} WIN!!!!")
        return True
    elif board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "0":
        print(f"Player {board[0]} WIN!!!!")
        return True
    elif board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "0":
        print(f"Player {board[2]} WIN!!!!")
        return True
    elif board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "0":
        print(f"Player {board[0]} WIN!!!!")
        return True
    elif board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[7] == "0":
        print(f"Player {board[1]} WIN!!!!")
        return True
    elif board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "0":
        print(f"Player {board[2]} WIN!!!!")
        return True
    else:
        return False
