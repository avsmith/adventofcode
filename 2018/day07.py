#!/usr/bin/env python

import re
from string import ascii_uppercase

file = open("day07.txt", "r")
text = file.read()
text = text.strip()
lines = text.split("\n")
steps = [x[5] + x[36] for x in lines]


def find_step(s, n=1):
    s.sort()
    second = set()
    for sx in s:
        snd = sx[1]
        second.add(snd)
    possible = []
    for lets in s:
        if lets[0] not in second:
            possible.append(lets[0])
    possible = reduce(possible)
    possible.sort()
    return possible[0:n]


def reduce(s):
    s = list(set(s))
    return s


path = ""
while len(steps) > 0:
    p = find_step(steps)
    regex = re.compile("^" + p[0])
    steps = [x for x in steps if not regex.match(x)]
    #  print((steps))
    path += p[0]
    if len(steps) == 1:
        path += steps[0]
        break

print(path)

secs = {}
for let in ascii_uppercase:
    secs[let] = ord(let) - 4


def secs_remaining(d):
    time = 0
    for key in d:
        time += d[key]
    return time


steps = [x[5] + x[36] for x in lines]
total_time = 0

path = ""
while secs_remaining(secs) > 0:
    total_time += 1
    pos = find_step(steps, 5)
    moves = []
    for s in pos:
        secs[s] -= 1
        if secs[s] <= 0:
            moves.append(s)
    if len(moves) > 0:
        path += moves[0]
        regex = re.compile("^" + moves[0])
        steps = [x for x in steps if not regex.match(x)]
    remaining_lets = [x for x in secs if secs[x] > 0]

    if len(remaining_lets) == 1:
        last_let = remaining_lets[0]
        path += last_let
        total_time += secs[last_let]
        secs[last_let] = 0

#  print(path)


print(path)
print(total_time)
