#!/usr/bin/env python

import os
import sys

decode = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

shape_score = {"rock": 1, "paper": 2, "scissors": 3}
result = {"win": 6, "tie": 3, "loss": 0}

winners = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
losers = {"paper": "rock", "scissors": "paper", "rock": "scissors"}


def rps(A, B):
    if A == B:
        return 3
    elif (
        (A == "scissors" and B == "rock")
        or (A == "paper" and B == "scissors")
        or (A == "rock" and B == "paper")
    ):
        return 6
    return 0


def score_rps(inA, inB, part1=True):
    convA = decode[inA]
    if part1:
        convB = decode[inB]
    else:
        if inB == "X":
            convB = losers[convA]
        elif inB == "Y":
            convB = convA
        elif inB == "Z":
            convB = winners[convA]

    game_score = 0
    #    print(convA, convB, shape_score[convB], rps(convA, convB))
    game_score += rps(convA, convB)
    game_score += shape_score[convB]
    return game_score


f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

score = 0

for line in input.splitlines():
    A, B = line.split(" ")
    score += score_rps(A, B)

print("Part1:", score)

score = 0

for line in input.splitlines():
    A, B = line.split(" ")
    score += score_rps(A, B, False)

print("Part2:", score)
