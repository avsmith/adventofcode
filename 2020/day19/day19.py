#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], "input19.txt"))
input = f.read()

rules, strings = [l.rstrip("\n") for l in input.split("\n\n")]

rules = dict([rule.split(": ", 1) for rule in rules.split("\n")])


def get_rule_re(rulenum, part2=False):
    if part2 is True:
        if rulenum == "8":
            return get_rule_re("42", part2) + "+"
        elif rulenum == "11":
            r42 = get_rule_re("42")
            r31 = get_rule_re("31")
            return (
                "(?:"
                + "|".join(f"{r42}{{{n}}}{r31}{{{n}}}" for n in range(1, 10))
                + ")"
            )

    rule = rules[rulenum]
    if re.fullmatch('"[ab]"', rule):
        return rule[1]
    else:
        parts = rule.split(" | ")
        res = []
        for part in parts:
            nums = part.split(" ")
            res.append("".join(get_rule_re(num, part2) for num in nums))
        return "(?:" + "|".join(res) + ")"


re_part1 = get_rule_re("0")
count = 0
for string in strings.split("\n"):
    count += bool(re.fullmatch(re_part1, string))
print("Part 1:", count)

re_part2 = get_rule_re("0", part2=True)
count2 = 0
for string in strings.split("\n"):
    count2 += bool(re.fullmatch(re_part2, string))
print("Part 2:", count2)
