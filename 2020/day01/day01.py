#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], 'input01.txt'))
data = f.read()

datai = [int(x) for x in data.splitlines()]

target = 2020

def report2(l,t):
  for i in l:
    for j in l:
      if i + j== t:
        return(i*j)

def report3(l,t):
  for i in l:
    for j in l:
      for k in l:
        if i + j + k== t:
          return(i*j*k)
  

print("Part 1 Answer:", report2(datai, target))
print("Part 2 Answer:", report3(datai, target))
