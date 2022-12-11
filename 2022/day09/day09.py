#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()


class Snake:
    def __init__(self, length):
        self.snake = [[0, 0] for x in range(length)]
        self.length = length
        self.tailstops = set()
        self.recordtail()

    def recordtail(self):
        self.tailstops.add((self.snake[-1][0], self.snake[-1][1]))

    def moveup(self, num):
        for _ in range(num):
            self.snake[0][1] += 1
            self.movesnake()

    def movedown(self, num):
        for _ in range(num):
            self.snake[0][1] -= 1
            self.movesnake()

    def moveright(self, num):
        for _ in range(num):
            self.snake[0][0] += 1
            self.movesnake()

    def moveleft(self, num):
        for _ in range(num):
            self.snake[0][0] -= 1
            self.movesnake()

    def movesnake(self):
        for i in range(1, len(self.snake)):
            # Test if next slot of snake has same X value, and
            # Y value is > 1 (should be 2!, not coded that way)
            if (
                self.snake[i - 1][0] == self.snake[i][0]
                and abs(self.snake[i - 1][1] - self.snake[i][1]) > 1
            ):
                # If so, move one position in Y direction
                self.snake[i][1] += int(
                    (self.snake[i - 1][1] - self.snake[i][1])
                    / abs(self.snake[i - 1][1] - self.snake[i][1])
                )
            # Test if next slot of snake has same Y value, and
            # X value is > 1 (should be 2!, not coded that way)
            elif (
                self.snake[i - 1][1] == self.snake[i][1]
                and abs(self.snake[i - 1][0] - self.snake[i][0]) > 1
            ):
                # If so, move one position in Y direction
                self.snake[i][0] += int(
                    (self.snake[i - i][0] - self.snake[i][0])
                    / abs(self.snake[i - i][0] - self.snake[i][0])
                )
            elif (
                # Test if one axis is more than 1 away. Due to rules
                # above, the other should also be 1 away.
                # Will exclude overlapping points (which do not move)
                abs(self.snake[i - 1][0] - self.snake[i][0]) > 1
                or abs(self.snake[i - 1][1] - self.snake[i][1]) > 1
            ):
                # If so, move on the diagonal by one in the appropriate
                # direction
                self.snake[i][1] += int(
                    (self.snake[i - 1][1] - self.snake[i][1])
                    / abs(self.snake[i - 1][1] - self.snake[i][1])
                )
                self.snake[i][0] += int(
                    (self.snake[i - 1][0] - self.snake[i][0])
                    / abs(self.snake[i - 1][0] - self.snake[i][0])
                )
            self.recordtail()


part1 = Snake(2)
part2 = Snake(10)

for line in input.splitlines():
    dir, n = line.split()
    n = int(n)
    if dir == "U":
        part1.moveup(n)
        part2.moveup(n)
    elif dir == "D":
        part1.movedown(n)
        part2.movedown(n)
    elif dir == "R":
        part1.moveright(n)
        part2.moveright(n)
    elif dir == "L":
        part1.moveleft(n)
        part2.moveleft(n)

print("Part1:", len(part1.tailstops))
print("Part2:", len(part2.tailstops))
