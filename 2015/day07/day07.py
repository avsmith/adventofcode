#!/usr/bin/env python

import os
import sys
import re
from collections import defaultdict


class Wire:
    def __init__(self, formula, value=-1):
        self.formula = formula
        self.value = value


f = open(os.path.join(sys.path[0], "input07.txt"))
data = f.read()
wires = data.splitlines()

testwires = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


instructions = {}
parse = re.compile("([^-]+) -> ([a-z]+)")
digits = re.compile(r"^[0-9]+$")

wires = defaultdict(defaultdict)

for line in testwires.splitlines():
    (input, outcome) = line.split(" -> ")
    if input.isdigit():
        value = int(input)
    else:
        value = None
    wires[outcome] = Wire(input, value)


need_calc = False
rounds = 0


while need_calc:
    starthash = hash(repr(instructions))
    for o in instructions:
        wire = instructions[o]["wire"]
        value = instructions[o]["value"]
        if value == -1:
            addition = re.match("([a-z0-9]+) AND ([a-z]+)", wire)
            if addition:
                (var1, var2) = addition.groups()
                m = digits.match(var1)
                if m:
                    val1 = int(m.group(0))
                else:
                    val1 = instructions[var1]["value"]
                val2 = instructions[var2]["value"]
                if val1 != -1 and val2 != -1:
                    res = val1 + val2
                    if res > 65535:
                        print(o, wire, val1, val2, res)
                        res = 0
                    instructions[o]["value"] = res
            lshift = re.match("([a-z]+) LSHIFT (\d+)", wire)
            if lshift:
                (var1, val1) = lshift.groups()
                if instructions[var1]["value"] != -1:
                    res = instructions[var1]["value"] << int(val1)
                    if (res) > 65535:
                        print(o, wire, val1, res)
                        res = 0
                        print(
                            o,
                            wire,
                        )
                    instructions[o]["value"] = res
            rshift = re.match("([a-z]+) RSHIFT (\d+)", wire)
            if rshift:
                (var1, val1) = rshift.groups()
                if instructions[var1]["value"] != -1:
                    res = instructions[var1]["value"] >> int(val1)
                    if (res) > 65535:
                        print(o, wire, val1, res)
                        res = 0
                    instructions[o]["value"] = res
            complement = re.match("NOT ([a-z]+)", wire)
            if complement:
                var1 = complement.group(1)
                if instructions[var1]["value"] != -1:
                    res = ~instructions[var1]["value"] & 65535
                    if res > 65535:
                        print(o, wire, instructions[var1]["value"], res)
                        res = 0
                    instructions[o]["value"] = res
            bitor = re.match("([a-z]+) OR ([a-z]+)", wire)
            if bitor:
                (var1, var2) = bitor.groups()
                if (
                    instructions[var1]["value"] != -1
                    and instructions[var2]["value"] != -1
                ):
                    res = instructions[var1]["value"] | instructions[var2]["value"]
                    if res > 65535:
                        print(o, wire, val1, val2, res)
                        res = 0
                    instructions[o]["value"] = res
            same = re.match("^([a-z]+)$", wire)
            if same:
                (var1) = same.group(0)
                res = instructions[var1]["value"]
                if res > 65535:
                    print(o, wire, res)
                    res = 0
                instructions[o]["value"] = res
            if (
                not bitor
                and not complement
                and not rshift
                and not addition
                and not lshift
                and not same
            ):
                print(o, wire)
    if hash(repr(instructions)) == starthash:
        need_calc = False

# print(instructions['a']['value'])
print(wires["g"].value)
print(wires["g"].formula)
