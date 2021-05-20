#!/usr/bin/env python


input = "10010000000110000"


def expand(string):
    left = string
    right = ""
    for c in reversed(string):
        if c == "0":
            right += "1"
        elif c == "1":
            right += "0"
        else:
            right += "X"
    return left + "0" + right


def dragonize(string, size):
    dragon = expand(string)
    while len(dragon) < size:
        dragon = expand(dragon)
    return dragon[0:size]


def checksum(string):
    check = string
    while len(check) % 2 == 0:
        new = ""
        for i in range(0, len(check), 2):
            if check[i] == check[i + 1]:
                new += "1"
            elif check[i] != check[i + 1]:
                new += "0"
        check = new
    return check


def dragon(input, size=272):
    expand = dragonize(input, size)
    return checksum(expand)


print("Part 1:", dragon(input))
print("Part 2:", dragon(input, 35651584))
