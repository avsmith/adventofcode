#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], 'input01.txt'))
data = f.read()

datai = [int(x) for x in data.splitlines()]

target = 2020


def report2(num, target):
  for i in num:
    for j in num:
      if i + j == target:
        return(i*j)


def report3(num, target):
  for i in num:
    for j in num:
      for k in num:
        if i + j + k == target:
          return(i*j*k)


print("Part 1 Answer:", report2(datai, target))
print("Part 2 Answer:", report3(datai, target))
