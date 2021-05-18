#!/usr/bin/env python

input = "yjdafjpo"

import hashlib

# from collections import deque, defaultdict


def makehash(seed, num):
    string = seed + str(num)
    return hashlib.md5(string.encode()).hexdigest()


def consecutive_character(string, number=3):
    letters = []
    for i in range(len(string) - number + 1):
        if string[i] == string[i + 1] and string[i] == string[i + 2]:
            return string[i]


def test_password(seed, letter, start):
    for i in range(start + 1, start + 1001):
        testpass = makehash(seed, i)
        for c in range(len(testpass) - 4):
            if (
                letter == testpass[c]
                and testpass[c] == testpass[c + 1]
                and testpass[c + 1] == testpass[c + 2]
                and testpass[c + 2] == testpass[c + 3]
                and testpass[c + 3] == testpass[c + 4]
            ):
                return True
    return False


def find_passwords(seed, needed=64):
    found = []
    round = 1
    while len(found) < needed:
        possiblepass = makehash(seed, round)
        consecutive = consecutive_character(possiblepass)
        if consecutive is not None:
            if test_password(seed, consecutive, round):
                found.append(round)
        round += 1
    return found[-1]


print("Part 1:", find_passwords(input))
