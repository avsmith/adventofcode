#!/usr/bin/env python


import string

TESTDATA = """\
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

DATA = """\
set b 81
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""


sounds = dict()

for char in list(string.ascii_lowercase[:8]):
    sounds[char] = 0
sounds["a"] = 1


instructions = DATA.splitlines()
inst = [x.split(" ") for x in instructions]

recover = False
pos = 0
note = 0
mul = 0
round = 0


def getnote(item, snds):
    if not item in snds.keys():
        return int(item)
    else:
        return snds[item]


while not recover:
    instruct = inst[pos][0]
    if instruct == "set":
        sounds[inst[pos][1]] = getnote(inst[pos][2], sounds)
        pos += 1
    elif instruct == "sub":
        sounds[inst[pos][1]] -= getnote(inst[pos][2], sounds)
        pos += 1
    elif instruct == "mul":
        sounds[inst[pos][1]] *= getnote(inst[pos][2], sounds)
        mul += 1
        pos += 1
    elif instruct == "jnz":
        value = inst[pos][1]
        if value.isdigit():
            value = int(value)
        else:
            value = sounds[inst[pos][1]]
        if value != 0:
            pos += getnote(inst[pos][2], sounds)
        else:
            pos += 1
    else:
        print("Missing", instruct)
        pos += 1
    round += 1
    #  print(pos)
    if round > 100:
        #    print(sounds)
        break
    print(round, sounds)
    #  print("{} {} {}".format(instruct, pos, sounds['a']))
    if pos >= len(inst):
        print("EXIT!")
        break
print(mul)
print(sounds["h"])

import sys

sys.exit()

b = c = d = e = f = g = h = 1
a = 1

# set b 81
# set c b
# jnz a 2
# jnz 1 5
# mul b 100
# sub b -100000
# set c b
# sub c -17000
# set f 1
# set d 2
# set e 2
# set g d
# mul g e
# sub g b
# jnz g 2
# set f 0
# sub e -1
# set g e
# sub g b
# jnz g -8
# sub d -1
# set g d
# sub g b
# jnz g -13
# jnz f 2
# sub h -1
# set g b
# sub g c
# jnz g 2
# jnz 1 3
# sub b -17
# jnz 1 -23
