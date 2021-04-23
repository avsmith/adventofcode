#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

tracking = []

for rule in input.splitlines():
    (action, amount) = rule.split(" ")
    tracking.append({"action": action, "amount": int(amount)})


def hand_held(tracker, loop=True):
    pos = 0
    acc = 0
    visited = set()
    while True:
        if pos in visited and loop is True:
            return acc
        elif pos in visited and loop is not True:
            raise RecursionError("Infinite Loop Detected")
        elif pos >= len(tracker):
            return acc
        else:
            visited.add(pos)
            if tracker[pos]["action"] == "jmp":
                pos += tracker[pos]["amount"]
            elif tracker[pos]["action"] == "acc":
                acc += tracker[pos]["amount"]
                pos += 1
            elif tracker[pos]["action"] == "nop":
                pos += 1
            else:
                print("ERROR")


def fix_code(t):
    for i in range(len(t)):
        if t[i]["action"] == "jmp":
            t[i]["action"] = "nop"
            try:
                return hand_held(t, False)
            except RecursionError:
                t[i]["action"] = "jmp"
        elif t[i]["action"] == "nop":
            t[i]["action"] = "jmp"
            try:
                return hand_held(t, False)
            except RecursionError:
                t[i]["action"] = "nop"


print(hand_held(tracking))
print(fix_code(tracking))
