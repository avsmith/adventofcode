#!/usr/bin/env python

import re
from collections import defaultdict

prog = """jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""


class Instruction:
    def __init__(self, input):
        self.instruction = input[0]
        self.register = input[1]
        if len(input) > 2:
            self.offset = int(input[2])
        else:
            self.offset = 0

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return f"{self.instruction} {self.register} {self.offset}"


program = list()

for line in prog.splitlines():
    items = re.split("[ ,]+", line)
    program.append(Instruction(items))


def run_program(instructions, part2=False):
    numbers = defaultdict(int)
    if part2:
        numbers["a"] = 1
    i = 0
    while i < len(instructions):
        step = instructions[i]
        instruct = step.instruction
        if instruct == "hlf":
            numbers[step.register] /= 2
            i += 1
        elif instruct == "tpl":
            numbers[step.register] *= 3
            i += 1
        elif instruct == "inc":
            numbers[step.register] += 1
            i += 1
        elif instruct == "jmp":
            i += int(step.register)
        elif instruct == "jie" and numbers[step.register] % 2 == 0:
            i += step.offset
        elif instruct == "jio" and numbers[step.register] == 1:
            i += step.offset
        else:
            i += 1
    return numbers["b"]


print("Part 1:", run_program(program))
print("Part 2:", run_program(program, True))
