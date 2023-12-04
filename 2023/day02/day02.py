#!/usr/bin/env python3

import os
import sys

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_digits(text):
    nums = "".join(c for c in text if c.isdigit())
    reduced = nums[0] + nums[-1]
    return int(reduced)


f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def illegal_ball(color, number):
    if int(number) > limits[color]:
        return True
    return False


def legal_game(balls):
    for b in balls.split(", "):
        num, color = b.split(" ")
        if illegal_ball(color, num):
            return False
    return True


score = 0

for line in input.splitlines():
    game, sets = line.split(": ")
    good = True
    for set in sets.split("; "):
        if legal_game(set) and good:
            good = True
        else:
            good = False
    if good:
        score += int(game[5:])

print("Part1:", score)


def game_score(sets):
    min_balls = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for balls in sets.split("; "):
        for b in balls.split(", "):
            num, color = b.split(" ")
            if min_balls[color] < int(num):
                min_balls[color] = int(num)
    return min_balls["red"] * min_balls["blue"] * min_balls["green"]


powers = 0

for line in input.splitlines():
    game, sets = line.split(": ")
    powers += game_score(sets)

print("Part2:", powers)
