#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input11.txt"))
input = f.read()

test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
    """


class Monkey:
    def __init__(self, name, items, operation, divisor, truedest, falsedest):
        self.name = name
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.truedest = truedest
        self.falsedest = falsedest
        self.inspected = 0

    def inspect(self):
        while self.items:
            old = self.items.pop(0)
            new = eval(self.operation)
            new //= 3
            if new % self.divisor == 0:
                recipient = next((m for m in monkeys if m.name == self.truedest), None)
            else:
                recipient = next((m for m in monkeys if m.name == self.falsedest), None)
            self.inspected += 1
            recipient.catch(new)

    def catch(self, worry):
        self.items.append(worry)

    def inspections(self):
        return self.inspected

    def __str__(self):
        items = ", ".join(str(x) for x in self.items)
        #        items = " ".join(self.items)
        string = f"""Monkey: {self.name}
Items: {items}
Divisor: {self.divisor}
Operation: {self.operation}
If True: {self.truedest}
If False: {self.falsedest}
Inspected: {self.inspected}
"""
        return string


def MakeMonkey(text):
    for line in text.splitlines():
        if "Monkey" in line:
            name = int(line[7:-1])
        elif "Starting items" in line:
            items = line[18:].split(", ")
            items = [int(x) for x in items]
        elif "Operation: new" in line:
            operation = line[19:]
        elif "Test: divisible by" in line:
            divisor = int(line[21:])
        elif "If true" in line:
            truedest = int(line[29:])
        elif "If false" in line:
            falsedest = int(line[30:])
    monkey = Monkey(name, items, operation, divisor, truedest, falsedest)
    return monkey


monkeys = []


for text in input.split("\n\n"):
    monkey = MakeMonkey(text)
    monkeys.append(monkey)
#    print(monkey)

for _ in range(20):
    for m in range(len(monkeys)):
        monkey = next((x for x in monkeys if x.name == m), None)
        monkey.inspect()


inspections = sorted([x.inspected for x in monkeys], reverse=True)
print("Part1:", inspections[0] * inspections[1])
