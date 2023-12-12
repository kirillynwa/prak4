import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
       4: (1, 0), 5: (1, 1), 6: (1, 2),
       7: (2, 0), 8: (2, 1), 9: (2, 2)}

pos1 = {(0, 0): 1, (0, 1): 2, (0, 2): 3,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
        (2, 0): 7, (2, 1): 8, (2, 2): 9}
x = []
y = []

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
    state = False
    try:
        if player == "O":
            with open("res.txt", "r") as file:
                line = file.readline()
                while line:
                    temp = str(position)
                    temp = temp[:-1]
                    index = line.find(temp, 0, len(temp))
                    if index == 0:
                        pos2 = int(line[len(temp) + 2])
                        if pos[pos2] in selection:
                            current_loc = pos[pos2]
                            state = True
                            break
                    line = file.readline()
        if state == False:
            current_loc = random.choice(selection)
        board[current_loc] = player
        position.append(pos1[current_loc])
        return (board, " ")
    except  Exception as e:
        return (board, "Draw")


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
                return ("Draw", board)
            counter += 1
            winner = evaluate(board)
            if winner != "0":
                break
    return (winner, board)
counter = 0
for i in range(10000):
    winner, board = play_game()
    if winner == 'O':
        with open("res.txt", "a") as output:
            print(str(position), file=output)
    with open("games.txt", "a") as output:
        print(str(board[0]), file=output)
        print(str(board[1]), file=output)
        print(str(board[2]), file=output)
        print("Winner is: " + winner, file=output)

    print(board[0])
    print(board[1])
    print(board[2])
    print("Winner is: " + winner)
    counter += 1
    x.append(counter)
    if winner == 'Draw':
        y.append('Draw')
    if winner == 'O':
        y.append('Win')
    if winner == 'X':
        y.append('Loss')
    position.clear()


plt.plot(x, y)
plt.xlabel('Количество шагов обучения')
plt.ylabel('Результат игры')
plt.title('График зависимостей')
plt.show()

# lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'winner']
# lists1 = ['1', '2', '3', '4']

# print(str(lists1)[:-1])
# with open("res.txt", "w") as output:
#     output.write(str(lists))
# with open("res.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         if str(lists1)[:-1] in line:
#             print("True")
#         line = file.readline()


# string = str(lists)
# index = string.find(str(lists1)[:-1], 0, len(str(lists1)[:-1]))
# print(index)
# print(string[len(str(lists1)[:-1])+3])
