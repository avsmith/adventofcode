#!/usr/bin/env python

import os
import sys
from collections import defaultdict

f = open(os.path.join(sys.path[0], "input12.txt"))
input = f.read()

instructions = []
values = defaultdict(int)

for line in input.splitlines():
    instructions.append(tuple(line.split()))


def run_code(part2=False):
    i = 0
    values = defaultdict(int)
    if part2:
        values["c"] = 1

    while i < len(instructions):
        instruction = instructions[i][0]
        register = instructions[i][1]
        try:
            dest = instructions[i][2]
        except IndexError:
            dest = None
        if instruction == "cpy":
            if register.isalpha():
                values[dest] = values[register]
            else:
                values[dest] = int(register)
        elif instruction == "inc":
            values[register] += 1
        elif instruction == "dec":
            values[register] -= 1
        elif instruction == "jnz" and (
            (register.isalpha() and values[register] != 0) or not register.isalpha()
        ):
            i += int(dest)
            continue
        i += 1
    return values["a"]


print("Part 1:", run_code())
print("Part 2:", run_code(True))
