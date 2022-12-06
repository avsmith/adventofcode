#!/usr/bin/env python

import os
import sys
from collections import deque

f = open(os.path.join(sys.path[0], "input05.txt"))
input = f.read()

setup, moves = input.split("\n\n")
setup = [l for l in setup.splitlines()]
moves = [l for l in moves.splitlines()]

elements = len(setup[-1].split())


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

    #    def stacks(self):
    #        return self.stacks

    def move(self, number, source, dest, new=False):
        for i in range(number):
            if new:
                pos = i
            else:
                pos = 0
            self.stacks[dest].insert(pos, self.stacks[source].popleft())

    def tops(self):
        x = "".join([x[0] for x in self.stacks])

        return x


stack = Stacks(setup)

# print(s.tops())
# print(s.stacks)


tracking = [deque() for _ in range(elements)]

for input in setup[0:-1]:
    for i in range(elements):
        pos = i * 4 + 1
        char = input[pos]
        if char != " ":
            tracking[i].append(char)


for move in moves:
    splits = move.split()
    number = int(splits[1])
    source = int(splits[3]) - 1
    dest = int(splits[5]) - 1
    for i in range(number):
        tracking[dest].insert(i, tracking[source].popleft())


print("Part1:", "".join([x[0] for x in tracking]))

# Part1: SBPQRSCDF
# Part2: RGLVRCQSB
