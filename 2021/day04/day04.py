#!/usr/bin/env python

import os
import sys
import numpy as np

f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()

data = input.splitlines()

moves = [int(x) for x in data[0].split(',')]

#print(len(data))
boards = []

for i in range(2, len(data), 6):
    board = []
    for row in data[i:i+5]:
        board = np.append(board, np.array(row.split(), dtype=np.int8))
    boards.append(board.reshape(5,5))


def check_bingo(card, calls):
    status = np.isin(card, calls)
    # "Diagonals don't count"
    # RTFM!!!
    #    if sum(status.diagonal()) == 5:
    #        return (True)
    #    if sum(np.fliplr(status).diagonal()) == 5:
    #        return (True)
    for j in range(5):
        if sum(status[j, :]) == 5:
            return (True)
        if sum(status[:, j]) == 5:
            return (True)
    return (False)


def find_winner(boards, moves):
    for i in range(len(moves)):
        called = moves[0:i+1]
        for board in boards:
            bingo = check_bingo(board, called)
            if bingo:
                return(board, called)


b, m = find_winner(boards, moves)
print("Part 1:", int(sum(b[np.where(~np.isin(b,m))])*m[-1]))
