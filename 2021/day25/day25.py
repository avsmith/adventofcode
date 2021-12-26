#!/usr/bin/env python

import sys
import os

import numpy as np

f = open(os.path.join(sys.path[0], "input25.txt"))
input = f.read()

grid = []

for line in input.splitlines():
    grid.append([x for x in line])

grid = np.array(grid)

# For debugging, print the grid
def print_grid(grid):
    header = ""
    for c in range(len(grid[0])):
        header += str(c % 10)
    print(header)
    for line in grid:
        print("".join(line))
    print("\n")


def make_move_right(array):
    # Create shifted array to find empty slots
    shiftl = np.roll(array, -1, axis=1)
    # Find positions for moving ">" and hold these
    moved = np.roll(np.where((shiftl == ".") & (array == ">"), ">", "."), 1, axis=1)
    # Find positions that can't move ">"
    unmoved = np.where((shiftl != ".") & (array == ">"), ">", ".")
    # Combine the moved and unmoved ">"
    newright = np.where((unmoved == ">") | (moved == ">"), ">", ".")
    # Take all ">" positions, otherwise the original
    final = np.where(array == "v", "v", newright)
    return final


def make_move_down(array):
    # Create shifted array to find empty slots
    shiftu = np.roll(array, -1, axis=0)
    # Find positions for moving "v" and hold these
    moved = np.roll(np.where((shiftu == ".") & (array == "v"), "v", "."), 1, axis=0)
    # Find positions that can't move "v"
    unmoved = np.where((shiftu != ".") & (array == "v"), "v", ".")
    # Combine the moved and unmoved "v"
    newdown = np.where((unmoved == "v") | (moved == "v"), "v", ".")
    # Take all "v" positions, otherwise the original
    final = np.where(array == ">", ">", newdown)
    return final


def find_stuck(array):
    count = 0
    while True:
        count += 1
        newarray = make_move_down(make_move_right(array))
        if np.array_equal(array, newarray):
            return count
        else:
            array = newarray


print("Part 1:", find_stuck(grid))
