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
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"""


sounds = dict()

for char in list(string.ascii_lowercase[:16]):
    sounds[char] = 0

instructions = DATA.splitlines()
inst = [x.split(" ") for x in instructions]

recover = False
pos = 0
note = 0


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
    elif instruct == "add":
        sounds[inst[pos][1]] += getnote(inst[pos][2], sounds)
        pos += 1
    elif instruct == "mul":
        sounds[inst[pos][1]] *= getnote(inst[pos][2], sounds)
        pos += 1
    elif instruct == "mod":
        sounds[inst[pos][1]] %= getnote(inst[pos][2], sounds)
        pos += 1
    elif instruct == "rcv":
        if sounds[inst[pos][1]] != 0:
            recover = True
        pos += 1
    elif instruct == "jgz":
        if sounds[inst[pos][1]] > 0:
            pos += getnote(inst[pos][2], sounds)
        else:
            pos += 1
    elif instruct == "snd":
        note = sounds[inst[pos][1]]
        pos += 1
    else:
        print("Missing", instruct)
        pos += 1
    #  print("{} {} {}".format(instruct, pos, sounds['a']))
    if pos >= len(inst):
        print("OOOOOPPPS!!!!")
        break

print(note)

### Star 2

sounds0 = dict()
sounds1 = dict()
send0 = 0
send1 = 0

for char in list(string.ascii_lowercase[:16]):
    sounds0[char] = 0
    sounds1[char] = 0

sounds1["p"] = 1
sounds0[1] = 0
sounds1[1] = 0
sounds0["1"] = 0
sounds1["1"] = 0
print(sounds1)


from collections import deque

notes0 = deque([])
notes1 = deque([])
pos0 = 0
pos1 = 0


def runprog(prog, sounds, inbox, outbox, count, pos):
    recover = False
    while not recover:
        instruct = prog[pos][0]
        if instruct == "set":
            #      print(prog[pos][2])
            #      print('set', getnote(prog[pos][2], sounds))
            sounds[prog[pos][1]] = getnote(prog[pos][2], sounds)
            pos += 1
        elif instruct == "add":
            sounds[prog[pos][1]] += getnote(prog[pos][2], sounds)
            pos += 1
        elif instruct == "mul":
            sounds[prog[pos][1]] *= getnote(prog[pos][2], sounds)
            pos += 1
        elif instruct == "mod":
            sounds[prog[pos][1]] %= getnote(prog[pos][2], sounds)
            pos += 1
        elif instruct == "rcv":
            if (len(inbox)) > 0:
                sounds[prog[pos][1]] = inbox.popleft()
            else:
                recover = True
            pos += 1
        elif instruct == "jgz":
            if sounds[prog[pos][1]] > 0:
                pos += getnote(prog[pos][2], sounds)
            else:
                pos += 1
        elif instruct == "snd":
            outbox.append(sounds[prog[pos][1]])
            #      print(outbox)
            pos += 1
            count += 1
        else:
            print("Missing", instruct)
            pos += 1
        if pos >= len(prog):
            print("OOOOOPPPS!!!!")
            break
    return (inbox, outbox, count, pos)


notes0, notes1, send0, pos0 = runprog(inst, sounds0, notes0, notes1, send0, pos0)

print(notes1)

import sys

sys.exit()

notes0, notes1, send1, pos1 = runprog(inst, sounds1, notes0, notes1, send1, pos1)

i = 0
while len(notes0) != 0 or len(notes1) != 0:
    notes1, notes0, send0, pos0 = runprog(inst, sounds0, notes1, notes0, send0, pos0)
    notes0, notes1, send1, pos1 = runprog(inst, sounds1, notes0, notes1, send1, pos1)
    print(
        "Round {} Notes0 {} Notes1 {}, Send0 {} Send1 {} Pos0 {} Pos1 {}".format(
            i, len(notes0), len(notes1), send0, send1, pos0, pos1
        )
    )
    i += 1

# print(notes0)
# print(notes1)


print(send0)
print(send1)
