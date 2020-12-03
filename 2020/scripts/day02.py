#!/usr/bin/env python

import re

f = open("data/input02.txt")
data = f.read()

array = data.splitlines()

def policy1(pw, let, cnta, cntb):
  ct = pw.count(let)
  if ct >= int(cnta) and ct <= int(cntb):
    return 1
  return 0

def policy2(pw, let, posa, posb):
  ret = (pw[int(posa)-1] == let) ^ (pw[int(posb)-1] == let)
  return(ret)

good_passwords1 = 0
good_passwords2 = 0

for txt in array:
   m = re.match(r"(\d+)-(\d+) (\w): (\w+)",txt)
   (num1, num2, letter, word) = m.groups()
   good_passwords1 += policy1(word, letter, num1, num2)
   good_passwords2 += policy2(word, letter, num1, num2)

print("Legal Password - Policy 1: ", good_passwords1)
print("Legal Passwords - Policy 2: ", good_passwords2)
