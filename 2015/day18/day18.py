#!/usr/bin/env python

import os
import sys
import numpy as np

testinput = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

f = open(os.path.join(sys.path[0], "input18.txt"))
input = f.read()

grid = [[1 if i == "#" else 0 for i in row] for row in input.splitlines()]


def neighbors(array):
    nrows = len(array)
    ncols = len(array[0])
    new = [[0 for i in range(ncols)] for j in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            current = array[i][j]
            lit = 0
            for ii in range(max(i - 1, 0), min(i + 2, nrows)):
                for jj in range(max(j - 1, 0), min(j + 2, ncols)):
                    lit += array[ii][jj]
            neighbor = lit - current
            if current == 1 and (neighbor == 2 or neighbor == 3):
                new[i][j] = 1
            elif current == 0 and neighbor == 3:
                new[i][j] = 1
    return new


for i in range(100):
    grid = neighbors(grid)

print("Part 1:", np.sum(grid))
