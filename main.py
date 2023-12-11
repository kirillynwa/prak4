import numpy as np
import random
import pandas as pd


pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
       4: (1, 0), 5: (1, 1), 6: (1, 2),
       7: (2, 0), 8: (2, 1), 9: (2, 2)}

pos1 = {(0, 0): 1, (0, 1): 2, (0, 2): 3,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
        (2, 0): 7, (2, 1): 8, (2, 2): 9}


def create_board():
    return (np.array([["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]))


def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "-":
                l.append((i, j))
    return (l)


# Select a random place for the player


def random_place(board, player):
    selection = possibilities(board)
    try:
        current_loc = random.choice(selection)
        board[current_loc] = player
        position.append(pos1[current_loc])
        return(board, " ")
    except:

        return(board, "Draw")



# Checks whether the player has three
# of their marks in a horizontal row


def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


# Checks whether the player has three
# of their marks in a vertical row


def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


# Checks whether the player has three
# of their marks in a diagonal row


def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win


# Evaluates whether there is
# a winner or a tie


def evaluate(board):
    winner = "0"

    for player in ["X", "O"]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = "-1"
    return winner


# Main function to start the game

position = []
def play_game():
    board, winner, counter = create_board(), "0", 1
    while winner == "0":
        for player in ["X", "O"]:
            board, res = random_place(board, player)
            if res == "Draw":
                return("Draw", board)
            counter += 1
            winner = evaluate(board)
            if winner != "0":
                break
    return (winner, board)


winner, board = play_game()
if winner != "Draw":
    count = 9 - len(position)
    for i in range(count):
        position.append("-")
    columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'winner']
    data = [[position[0], position[1], position[2], position[3], position[4], position[5], position[6], position[7], position[8], winner]]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('res.csv', mode='a', header=False, index=False)
# print(board[0])
# print(board[1])
# print(board[2])
#
# print("Winner is: " + winner)

