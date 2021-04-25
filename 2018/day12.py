#!/usr/bin/env python

import re

input1 = """.#.## => .
.#### => .
#..#. => .
##.## => #
..##. => #
##... => #
..#.. => #
#.##. => .
##.#. => .
.###. => #
.#.#. => #
#..## => #
.##.# => #
#.### => #
.##.. => #
###.# => .
#.#.# => #
#.... => .
#...# => .
.#... => #
##..# => .
....# => .
..... => .
.#..# => #
##### => .
#.#.. => .
..#.# => #
...## => .
...#. => #
..### => .
####. => #
###.. => #"""

growth = dict()

for x in input1.split("\n"):
    t, o = x.split(" => ")
    growth[t] = o

code = "#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##"
leftpad = 0

for i in range(20):
    code = "..." + code + "..."
    newcode = ""
    leftpad += 1
    for x in range(len(code) - 4):
        key = code[x : x + 5]
        newcode += growth[key]
    code = newcode
    leftdot = len(re.search("^\.+|$", code).group())
    leftpad -= leftdot
    rightdot = len(re.search("\.+$|$", code).group())
    code = code[leftdot : len(code) - rightdot]

score = 0
for x in range(len(code)):
    if code[x] == "#":
        score += x - leftpad

print(score)


code = "#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##"
endpoint = True
imax = 150
leftpad = 0
i = 0
seen = dict()


def do_grow(c):
    startlen = len(c)
    paddedcode = "..." + c + "..."
    newcode = ""
    for x in range(len(paddedcode) - 4):
        key = paddedcode[x : x + 5]
        newcode += growth[key]
    newcode = re.sub("^\.+", "", newcode)
    leftdot = len(re.search("^\.+|$", newcode).group())
    #  print(leftdot)
    newcode = re.sub("\.+$", "", newcode)
    #  print(len(newcode),startlen)
    return newcode


while endpoint is True:
    newcode = do_grow(code)
    #  print(code)
    #  print(newcode)
    if (newcode) == code:
        print("REPEAT")
    if i > imax - 2:
        endpoint = False
    i += 1


score = 0
for x in range(len(code)):
    if code[x] == "#":
        score += x - leftpad
# Not working
print(score)
