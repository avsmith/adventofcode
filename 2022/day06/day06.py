#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input06.txt"))
input = f.read()


def uniq_chars(word):
    chars = [*word]
    return len(chars) == len(set(chars))


def marker(word, length=4):
    for i in range(len(input) - length + 1):
        test = input[i : i + length]
        if uniq_chars(test):
            return i + length
    return -1


print("Part1:", marker(input))
print("Part2:", marker(input, 14))
