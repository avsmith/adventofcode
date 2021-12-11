#!/usr/bin/env python

import os
import sys

import numpy as np

f = open(os.path.join(sys.path[0], "input10.txt"))
input = f.read()

def pair_replace(string):
    string = string.replace("{}", "").replace("[]", "").replace("<>", "").replace("()", "")
    return string

def left_replace(string):
    string = string.replace("{", "").replace("[", "").replace("<", "").replace("(", "")
    return string

def full_pair_replace(string):
    replaced = pair_replace(string)
    if replaced == string:
        return string
    else:
        return full_pair_replace(replaced)

def full_left_replace(string):
    replaced = left_replace(string)
    if replaced == string:
        return string
    else:
        return full_left_replace(replaced)


def fix_string(string):
    # Recursively replaces pairs of character
    reduced = full_pair_replace(string)
    # Recurrively replaces first left bracket
    leftgone= full_left_replace(reduced)
    return reduced, leftgone


def fix_score(string):
    fixable = full_pair_replace(string)
    score = 0

    # ): 1 point.
    # ]: 2 points.
    # }: 3 points.
    # >: 4 points.

    for i in range(-1,-1*(len(fixable)+1),-1):
        c = fixable[i]
        if c == "(":
            score *= 5
            score += 1
        elif c == "[":
            score *= 5
            score += 2
        elif c == "{":
            score *= 5
            score += 3
        elif c == "<":
            score *= 5
            score += 4
    return score

def string_error(string):
    reduced, leftgone = fix_string(string)

    first = leftgone[:1]

    if first == ")":
        return 3
    elif first=="]":
        return 57
    elif first=="}":
        return 1197
    elif first==">":
        return 25137
    return 0

fix_scores = []
total = 0

for line in input.splitlines():
    err = string_error(line)

    if err == 0:
        fix_scores.append(fix_score(line))
    total += err

print("Part 1:", total)
print("Part 2:", int(np.median(fix_scores)))
