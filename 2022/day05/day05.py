#!/usr/bin/env python

import os
import sys
from collections import deque

f = open(os.path.join(sys.path[0], "input05.txt"))
input = f.read()

setup, moves = input.split("\n\n")
setup = [l for l in setup.splitlines()]
moves = [l for l in moves.splitlines()]


class Stacks:
    def __init__(self, setup, part2=False):
        elements = len(setup[-1].split())
        self.stacks = [deque() for _ in range(elements)]
        self.part2 = part2
        for input in setup[0:-1]:
            for i in range(elements):
                pos = i * 4 + 1
                char = input[pos]
                if char != " ":
                    self.stacks[i].append(char)

    def move(self, number, source, dest):
        for i in range(number):
            if self.part2:
                pos = i
            else:
                pos = 0
            self.stacks[dest].insert(pos, self.stacks[source].popleft())

    def tops(self):
        tops = "".join([x[0] for x in self.stacks])
        return tops


part1 = Stacks(setup)
part2 = Stacks(setup, True)


for move in moves:
    splits = move.split()
    number = int(splits[1])
    source = int(splits[3]) - 1
    dest = int(splits[5]) - 1
    part1.move(number, source, dest)
    part2.move(number, source, dest)

print("Part1:", part1.tops())
print("Part2:", part2.tops())

# Part1: SBPQRSCDF
# Part2: RGLVRCQSB
