#!/usr/bin/env python

import os
import sys
import pprint
from collections import defaultdict


class Wire:
    def __init__(self, function, inputa=None, inputb=None, value=-1):
        self.function = function
        self.value = value
        self.inputa = inputa
        self.inputb = inputb

    def __repr__(self):
        return f"{{Func: {self.function}; A: {self.inputa}; B: {self.inputb}; Value: {self.value}}}"


def return_value(wire):
    #    print(f"{wire.function} {wire.inputa} {wire.inputb}")
    if wire.value is not None:
        return wire.value
    else:
        wire.value = evaluate_formula(wire.function, wire.inputa, wire.inputb)
        return wire.value


def evaluate_formula(form, ina, inb):
    #    print(form, ina, inb)
    #    print(form)
    if form == "EQUAL":
        if ina.isdigit():
            return int(ina)
        else:
            return return_value(wires[ina])
    elif form == "AND":
        if ina.isdigit():
            a = int(ina)
        else:
            a = return_value(wires[ina])
        b = return_value(wires[inb])
        ret = a & b
        return ret
    elif form == "OR":
        a = return_value(wires[ina])
        b = return_value(wires[inb])
        ret = a | b
        return ret
    elif form == "LSHIFT":
        a = return_value(wires[ina])
        ret = a << int(inb)
        return ret
    elif form == "RSHIFT":
        a = return_value(wires[ina])
        ret = a >> int(inb)
        return ret
    elif form == "NOT":
        a = return_value(wires[ina])
        ret = ~a & 65535
        return ret
    return "ERROR"


pp = pprint.PrettyPrinter(indent=4)

f = open(os.path.join(sys.path[0], "input07.txt"))
data = f.read()

testdata = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

wires = defaultdict(defaultdict)

for line in data.splitlines():
    (input, outcome) = line.split(" -> ")
    words = input.split(" ")
    value = None
    if len(words) == 1:
        function = "EQUAL"
        inputa = words[0]
        inputb = None
        if words[0].isdigit():
            value = int(words[0])
    elif len(words) == 2:
        function = words[0]
        inputa = words[1]
        inputb = None
    elif len(words) == 3:
        inputa = words[0]
        function = words[1]
        inputb = words[2]
    wires[outcome] = Wire(function, inputa, inputb, value)


# pp.pprint(wires)
print("Part 1:", return_value(wires["a"]))

# for x in sorted(wires):
#    print(x, return_value(wires[x]))
# pp.pprint(wires)
