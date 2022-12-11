#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()

test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


class Snake:
    def __init__(self):
        self.head = {"x": 0, "y": 0}
        self.tail = {"x": 0, "y": 0}
        #        self.headvisited = set()
        self.tailstops = set()
        self.recordtail(0, 0)

    def moveup(self, num):
        for _ in range(num):
            self.head["y"] += 1
            self.movetail()

    def movedown(self, num):
        for _ in range(num):
            self.head["y"] -= 1
            self.movetail()

    def moveright(self, num):
        for _ in range(num):
            self.head["x"] += 1
            self.movetail()

    def moveleft(self, num):
        for _ in range(num):
            self.head["x"] -= 1
            self.movetail()

    def movetail(self):
        if (
            self.head["x"] == self.tail["x"]
            and abs(self.head["y"] - self.tail["y"]) > 1
        ):
            self.tail["y"] += (self.head["y"] - self.tail["y"]) / abs(
                self.head["y"] - self.tail["y"]
            )
        elif (
            self.head["y"] == self.tail["y"]
            and abs(self.head["x"] - self.tail["x"]) > 1
        ):
            self.tail["x"] += (self.head["x"] - self.tail["x"]) / abs(
                self.head["x"] - self.tail["x"]
            )
        elif (
            abs(self.head["x"] - self.tail["x"]) > 1
            or abs(self.head["y"] - self.tail["y"]) > 1
        ):
            self.tail["x"] += (self.head["x"] - self.tail["x"]) / abs(
                self.head["x"] - self.tail["x"]
            )
            self.tail["y"] += (self.head["y"] - self.tail["y"]) / abs(
                self.head["y"] - self.tail["y"]
            )
        self.recordtail(int(self.tail["x"]), int(self.tail["y"]))

    def recordtail(self, x, y):
        self.tailstops.add((x, y))


part1 = Snake()

for line in input.splitlines():
    dir, n = line.split()
    n = int(n)
    if dir == "U":
        part1.moveup(n)
    elif dir == "D":
        part1.movedown(n)
    elif dir == "R":
        part1.moveright(n)
    elif dir == "L":
        part1.moveleft(n)

print(len(part1.tailstops))
