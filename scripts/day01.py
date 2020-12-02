#!/usr/bin/env python

f = open("data/input01.txt")
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
  

print("Report 2 Answer:", report2(datai, target))
print("Report 3 Answer:", report3(datai, target))
