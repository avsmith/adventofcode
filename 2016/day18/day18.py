#!/usr/bin/env python

input = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"


def traps(string):
    new = ""
    for i in range(len(string)):
        if i == 0:
            l = "."
        else:
            l = string[i - 1]
        if i == len(string) - 1:
            r = "."
        else:
            r = string[i + 1]
        if l == r:
            new += "."
        else:
            new += "^"
    return new


def rogue(string, rounds):
    total = string.count(".")
    for i in range(rounds - 1):
        string = traps(string)
        total += string.count(".")
    return total


print("Part 1:", rogue(input, 40))
print("Part 2:", rogue(input, 400000))
