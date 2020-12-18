#!/usr/bin/env python

testinput='''F10
N3
F7
R90
F11
'''

import os, sys

f = open(os.path.join(sys.path[0], 'input12.txt'))
input = f.read()

position = 0+0j
position2 = 0+0j
direction = 1
waypoint = 10+1j

for item in input.splitlines():
  instruction = item[0]
  amount = int(item[1:])
  if instruction == 'N':
    position += amount * 1j
    waypoint += amount * 1j
  elif instruction == 'S':
    position -= amount * 1j
    waypoint -= amount * 1j  
  elif instruction == 'E':
    position += amount
    waypoint += amount
  elif instruction == 'W':
    position -= amount
    waypoint -= amount
  elif instruction == 'F':
    position += direction * amount
    position2 += waypoint * amount
  elif instruction == 'R':
    turns = amount/90
    turn_factor = 1j**(4-turns%4)
    direction *= turn_factor
    waypoint = waypoint.real*turn_factor + waypoint.imag*turn_factor*1j
  elif instruction == 'L':
    turns = amount/90
    turn_factor = 1j**(turns%4)
    direction *= turn_factor
    waypoint = waypoint.real*turn_factor + waypoint.imag*turn_factor*1j
  else:
    raise Error("Ooops")

print(int(abs(position.real)+abs(position.imag)))
print(int(abs(position2.real)+abs(position2.imag)))
