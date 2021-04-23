#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], "input04.txt"))
data = f.read()

# Convert to list of dick objects
items = [
    dict(v.split(":") for v in entry)
    for entry in [x.replace("\n", " ").split(" ") for x in data.split("\n\n")]
]

# Valid data rules:
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


hclre = re.compile(r"^#[a-f0-9]{6,6}$")
pidre = re.compile(r"^[0-9]{9,9}$")
hgtre = re.compile(r"(\d+)(in|cm)")

eyecols = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid = 0
good = 0


def check_validity(it):
    if int(it["byr"]) < 1920 or int(it["byr"]) > 2002:
        return 0
    if int(it["iyr"]) < 2010 or int(it["iyr"]) > 2020:
        return 0
    if int(it["eyr"]) < 2020 or int(it["eyr"]) > 2030:
        return 0
    m = hgtre.match(it["hgt"])
    if type(m) == type(None):
        return 0
    (val, unit) = m.groups()
    if (unit == "in" and (int(val) < 59 or int(val) > 76)) or (
        unit == "cm" and (int(val) < 150 or int(val) > 193)
    ):
        return 0
    if not hclre.match(it["hcl"]):
        return 0
    if it["ecl"] not in eyecols:
        return 0
    if not pidre.match(it["pid"]):
        return 0
    return 1


for item in items:
    ret = item.pop("cid", None)
    if len(item) == 7:
        valid += 1
        if not check_validity(item):
            continue
        good += 1


print("Part 1 (Valid 7 fields):", valid)
print("Part 2 (All data valid):", good)
