#!/usr/bin/env python

import sys
import os

import numpy as np

test = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

f = open(os.path.join(sys.path[0], "input25.txt"))
input = f.read()

grid = []

for line in input.splitlines():
    arr = []
    for x in line:
        if x == "v":
            arr.append(1)
        elif x == ">":
            arr.append(-1)
        else:
            arr.append(0)

    grid.append(arr)
grid = np.array(grid)


def print_grid(grid):
    header = ""
    for c in range(len(grid[0])):
        header += str(c % 10)
    print(header)
    for line in grid:
        string = ""
        for c in line:
            if c == -1:
                string += ">"
            elif c == 1:
                string += "v"
            else:
                string += "."
        print(string)
    print("\n")


def make_move_right(array):
    shiftl = np.roll(array, -1, axis=1)
    moved = np.roll(np.where((shiftl == 0) & (array == -1), -1, 0), 1, axis=1)
    unmoved = np.where((shiftl != 0) & (array == -1), -1, 0)
    newright = np.where((unmoved == -1) | (moved == -1), -1, 0)
    final = np.where(array == 1, 1, newright)
    return final


def make_move_down(array):
    shiftu = np.roll(array, -1, axis=0)
    moved = np.roll(np.where((shiftu == 0) & (array == 1), 1, 0), 1, axis=0)
    unmoved = np.where((shiftu != 0) & (array == 1), 1, 0)
    newdown = np.where((unmoved == 1) | (moved == 1), 1, 0)
    final = np.where(array == -1, -1, newdown)
    return final


def find_stuck(array):
    count = 0
    while count < 1000:
        count += 1
        newarray = make_move_down(make_move_right(array))
        if np.array_equal(array, newarray):
            return count
        else:
            array = newarray


print("Part 1:", find_stuck(grid))
