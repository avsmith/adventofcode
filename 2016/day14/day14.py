#!/usr/bin/env python

input = "yjdafjpo"

import hashlib

from collections import defaultdict


def makehash(seed, num, salt=1):
    string = seed + str(num)
    for i in range(0, salt):
        string = hashlib.md5(string.encode()).hexdigest()
    return string


def consecutive_character(string, number=3):
    letters = []
    for i in range(len(string) - number + 1):
        if string[i] == string[i + 1] and string[i] == string[i + 2]:
            return string[i]


def test_password(hashes, seed, letter, start, salt=1):
    for i in range(start + 1, start + 1001):
        try:
            testpass = hashes[i]
        except KeyError:
            hashes[i] = makehash(seed, i, salt)
            testpass = hashes[i]
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


def find_passwords(seed, salt=1):
    found = []
    round = 0
    needed = 64
    hashes = defaultdict()
    while len(found) < needed:
        try:
            possiblepass = hashes[round]
        except KeyError:
            hashes[round] = makehash(seed, round, salt)
            possiblepass = hashes[round]
        consecutive = consecutive_character(possiblepass)
        if consecutive is not None:
            if test_password(hashes, seed, consecutive, round, salt):
                found.append(round)
        round += 1
    return found[-1]


print("Part 1:", find_passwords(input))
print("Part 2:", find_passwords(input, 2017))
