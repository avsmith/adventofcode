#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], 'input03.txt'))
data = f.read()

houses = [[0,0]]
santa = [[0,0]]
robo = [[0,0]]


for i in range(len(data)):
  move = data[i]
  (ns, ew) = houses[-1]
  (sns, sew) = santa[-1]
  (rns, rew) = robo[-1]
  if move == '^':
    ns += 1
    if i % 2 == 0:
      sns += 1
    else:
      rns += 1
  if move == 'v':
    ns -= 1
    if i % 2 == 0:
      sns -= 1
    else:
      rns -= 1
  if move == '<':
    ew -= 1
    if i % 2 == 0:
      sew -= 1
    else:
      rew -= 1
  if move == '>':
    ew += 1
    if i % 2 == 0:
      sew += 1
    else:
      rew += 1
  houses.append([ns,ew])
  santa.append([sns,sew])
  robo.append([rns,rew])



num_houses = len(set([tuple(h) for h in houses]))
print("Houses year 1:", num_houses)
num_houses_year2 = len(set([tuple(h) for h in santa + robo]))

print("Houses year 2:", num_houses_year2)
