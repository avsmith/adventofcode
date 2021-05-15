#!/usr/bin/env python

import os
import sys

import re

f = open(os.path.join(sys.path[0], "input07.txt"))
input = f.read()


def abba(word):
    for i in range(len(word) - 3):
        if (
            word[i] == word[i + 3]
            and word[i] != word[i + 1]
            and word[i + 1] == word[i + 2]
        ):
            return True
    return False


def skip(outside, inside):
    for outw in outside:
        for i in range(len(outw) - 2):
            if outw[i] == outw[i + 2] and outw[i] != outw[i + 1]:
                for inw in inside:
                    for j in range(len(inw) - 2):
                        if inw[j + 1] == outw[i] and inw[j] == outw[i + 1]:
                            return True
    return False


def aba(words):
    legal = []
    for word in words:
        for i in range(len(word) - 2):
            if word[i] == word[i + 2] and word[i] != word[i + 1]:
                legal.append([word[i], word[i + 1]])
    return legal


def bab(words, leta, letb):
    for word in words:
        for i in range(len(word) - 2):
            if word[i] == letb and word[i + 1] == leta and word[i + 2] == letb:
                return True
    return False


tls = 0
ssl = 0

for line in input.splitlines():
    code = re.split("\[|\]", line)
    if any([abba(x) for x in code[0::2]]) and not any([abba(x) for x in code[1::2]]):
        tls += 1
    aba_seen = aba(code[0::2])
    if any([bab(code[1::2], let[0], let[1]) for let in aba_seen]):
        ssl += 1

print("Part 1:", tls)
print("Part 2:", ssl)
