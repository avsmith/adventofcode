#!/usr/bin/env python

import re
import os, sys
from collections import defaultdict

MOVES = {"e": 1, "se": 1 - 1j, "sw": 0 - 1j, "w": -1, "nw": -1 + 1j, "ne": 1j}

movere = re.compile("(" + "|".join(MOVES.keys()) + ")")

f = open(os.path.join(sys.path[0], "input24.txt"))
input = f.read()

starttiles = defaultdict(lambda: 1)

for line in input.splitlines():
    pos = 0 + 0j
    moves = movere.findall(line)
    for move in moves:
        pos += MOVES[move]
    starttiles[pos] *= -1

part1 = [pos for pos, x in starttiles.items() if x == -1]
print(len(part1))

# for part2

seedtiles = [pos for pos, x in starttiles.items() if x == -1]


def find_neighbors(pos):
    neighbors = []
    for dir in MOVES.values():
        neighbors.append(pos + dir)
    return neighbors


def flip_tiles(blacktiles, n):
    for i in range(n):
        checktiles = set(blacktiles)
        newtiles = []
        for pos in blacktiles:
            checktiles.update(find_neighbors(pos))
        for tile in set(checktiles):
            numneighbors = sum(n in blacktiles for n in find_neighbors(tile))
            if tile in blacktiles:
                if numneighbors in (1, 2):
                    newtiles.append(tile)
            elif tile not in blacktiles:
                if numneighbors == 2:
                    newtiles.append(tile)
        blacktiles = newtiles
    return blacktiles


part2 = flip_tiles(part1, 100)
print(len(part2))
