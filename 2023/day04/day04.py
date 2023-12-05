#!/usr/bin/env python3

import os
import sys

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()

score = 0


def count_winners(card):
    c, numbers = card.split(": ")
    winning_nums, my_nums = numbers.split(" | ")
    winners = winning_nums.split()
    matches = 0
    for my_num in my_nums.split():
        if my_num in winners:
            matches += 1
    return matches


tracker = list()

for card in input.splitlines():
    matches = count_winners(card)
    tracker.append(matches)
    if matches > 0:
        score += 2 ** (matches - 1)

print("Part1", score)

ticket_counts = [1] * len(tracker)


for i in range(len(tracker)):
    tix = ticket_counts[i]
    winners = tracker[i]
    for j in range(i + 1, winners + i + 1):
        for _ in range(tix):
            ticket_counts[j] += 1

print("Part2:", sum(ticket_counts))
