#!/usr/bin/env python

import os
import sys
import numpy as np

f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()

data = input.splitlines()

moves = [int(x) for x in data[0].split(',')]

boards = []

for i in range(2, len(data), 6):
    board = []
    for row in data[i:i+5]:
        board = np.append(board, np.array(row.split(), dtype=np.int8))
    boards.append(board.reshape(5, 5))


def check_bingo(card, calls):
    status = np.isin(card, calls)
    for j in range(5):
        if sum(status[j, :]) == 5:
            return (True)
        if sum(status[:, j]) == 5:
            return (True)
    return (False)


def find_first(boards, moves):
    for i in range(len(moves)):
        called = moves[0:i+1]
        for board in boards:
            bingo = check_bingo(board, called)
            if bingo:
                return(board, called)


def find_last(boards, moves):
    last = False
    for i in range(len(moves)):
        losers = []
        called = moves[0:i+1]
        for board in boards:
            bingo = check_bingo(board, called)
            if not bingo:
                losers.append(board)
            if last and bingo:
                return(board, called)
        if len(losers) == 1:
            last = True
        boards = losers


def board_score(board, moves):
    remaining_positions = np.where(~np.isin(board, moves))
    remaining_numbers = board[remaining_positions]
    last_move = moves[-1]
    return(int(sum(remaining_numbers) * last_move))


b, m = find_first(boards, moves)
print("Part 1:", board_score(b, m))
b2, m2 = find_last(boards, moves)
print("Part 2:", board_score(b2, m2))
