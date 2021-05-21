#!/usr/bin/env python

input = 3014603

from collections import deque


def seed_elves(num):
    start = deque()
    for i in range(num):
        start.append(i + 1)
    return start


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


def find_elf(num, part2=False):
    elves = seed_elves(num)
    while len(elves) > 1:
        if part2:
            target = num // 2
        else:
            target = 1
        delete_nth(elves, target)
        elves.rotate(-1)
        num -= 1
    return elves[0]


print("Part 1:", find_elf(5))
print("Part 2:", find_elf(5, True))
