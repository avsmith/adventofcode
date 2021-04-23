#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], "input03.txt"))
data = f.read()


def reverse(string):
    string = string[::-1]
    return string


testdata = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

orig = data.splitlines()


def trees_hit(slope, right=3, down=1, debug=False):
    trees = 0
    for y in range(0, len(slope), down):
        slopeline = slope[y]
        x = (y // down * right) % len(slopeline)

        # Checking bit positions via shift rather than character check
        # Trying to learn something...
        slopeint = int(reverse(slopeline.replace("#", "1").replace(".", "0")), 2)
        pos = slopeint >> x
        trees += pos & 1 == 1

        if debug:
            if slopeline[x] == "#":
                newline = slopeline[:x] + "X" + slopeline[x + 1 :]
            else:
                newline = slopeline[:x] + "O" + slopeline[x + 1 :]
            print(slopeline, newline)
    return trees


print("Part 1 answer:", trees_hit(orig))
print(
    "Part 2 answer:",
    trees_hit(orig, 1, 1)
    * trees_hit(orig, 3, 1)
    * trees_hit(orig, 5, 1)
    * trees_hit(orig, 7, 1)
    * trees_hit(orig, 1, 2),
)
