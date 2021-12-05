#!/usr/bin/env python

import re
import numpy as np

import os
import sys

f = open(os.path.join(sys.path[0], "input05.txt"))
input = f.read()

movesre = re.compile("(\\d+),(\\d+) -> (\\d+),(\\d+)")

moves = np.array([], dtype='i8')

for line in input.splitlines():
    movesmatch = movesre.match(line)
    if movesmatch:
        (x1, y1, x2, y2) = movesmatch.groups()

        moves = np.append(moves, np.array([int(x1), int(y1),
            int(x2), int(y2)]))

moves = moves.reshape(int(len(moves)/4), 4)


def find_overlap(moves, diag=False):
    maxval = int(np.amax(moves))
    board = np.zeros((maxval+1, maxval+1))

    for x1, y1, x2, y2 in moves:
        if x2 > x1:
            xstep = 1
        elif x2 < x1:
            xstep = -1
        else:
            xstep = 0
        if y2 > y1:
            ystep = 1
        elif y2 < y1:
            ystep = -1
        else:
            ystep = 0
        steps = max(abs(x2-x1), abs(y2-y1)) + 1
        if not diag and xstep != 0 and ystep != 0:
            continue
        for delta in range(steps):
            x = x1 + xstep*delta
            y = y1 + ystep*delta
            board[y, x] += 1

#    print(board)
    positions = np.where(board > 1)
    return(len(positions[0]))


print("Part 1:", find_overlap(moves))
print("Part 2:", find_overlap(moves, True))
