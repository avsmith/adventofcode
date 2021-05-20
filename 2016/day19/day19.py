#!/usr/bin/env python

input = 3014603


def seed_elves(num):
    start = dict()
    for i in range(num):
        start[i + 1] = 1
    return start


def find_elf(num, part2=False):
    elves = seed_elves(num)
    presents = [k for k in elves if elves[k] > 0]
    while len(presents) > 1:
        for i in range(len(presents)):
            if i == len(presents) - 1 and elves[presents[i]] > 0:
                elves[presents[i]] += elves[presents[0]]
                elves[presents[0]] = 0
            elif elves[presents[i]] > 0:
                elves[presents[i]] += elves[presents[i + 1]]
                elves[presents[i + 1]] = 0
        presents = [k for k in elves if elves[k] > 0]
    return presents[0]


print("Part 1:", find_elf(input))
