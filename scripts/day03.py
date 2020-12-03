#!/usr/bin/env python

def reverse(string): 
  string = string[::-1] 
  return string 

f = open("data/input03.txt")
data = f.read()

offset = 3

orig = data.splitlines()
length = len(orig[0])
array = [int(reverse(s.replace('#','1').replace('.','0')),2) for s in orig]

trees = 0 

for y in range(len(array)):
  x = (y * offset) % length 
  pos = array[y] >> x
  trees +=  pos&1==1

print("Part 1 answer:", trees)
