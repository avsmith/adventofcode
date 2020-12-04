#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], 'input04.txt'))
data = f.read()

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

items = [x.replace('\n',' ').split(' ') for x in data.split('\n\n')]
items = [dict(e.split(':') for e in li) for li in items]
items2 = [dict(v.split(':') for v in entry) for entry in [x.replace('\n',' ').split(' ') for x in data.split('\n\n')]]

colpat = re.compile("^#[a-f0-9]{6,6}$")
eyecols = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
passpat = re.compile("^[0-9]{9,9}$")

valid = 0 
good = 0
for item in items2:
  ret = item.pop('cid',None)
  if len(item) == 7:
    valid += 1
    if int(item['byr']) < 1920 or int(item['byr']) > 2002:
      continue
    if int(item['iyr']) < 2010 or int(item['iyr']) > 2020:
      continue
    if int(item['eyr']) < 2020 or int(item['eyr']) > 2030:
      continue
    m = re.match(r"(\d+)(in|cm)",item['hgt'])
    if type(m) == type(None):
      continue
    (val, unit) = m.groups()
    if (unit == 'in' and (int(val) <59 or int(val) > 76)) or (unit == 'cm' and (int(val) <150 or int(val) > 193)):
      continue
    if not colpat.match(item['hcl']):
      continue
    if  item['ecl'] not in eyecols:
      continue
    if not passpat.match(item['pid']):
      continue    
    good += 1



print("Valid 7 fields:", valid)
print("All data valid:", good)
