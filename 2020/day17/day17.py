#!/usr/bin/env python

from collections import defaultdict
from itertools import product
import copy
import numpy as np

dirs = tuple(product([-1,0,1], repeat=3))
dirs4d = tuple(product([-1,0,1], repeat=4))
#print(np.array(dirs))
#universe = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

def makehash():
  return defaultdict(makehash)

universe= makehash()

testinput = '''.#.
..#
###'''

input = '''##..####
.###....
#.###.##
#....#..
...#..#.
#.#...##
..#.#.#.
.##...#.
'''

input = [[1 if i == '#' else 0  for i in row] for row in input.splitlines()]

universe = np.zeros((1,len(input),len(input[0])))
universe4d = np.zeros((1,1,len(input),len(input[0])))

for d1 in range(len(input)):
  for d2 in range(len(input[d1])):
    if input[d1][d2] == 1:
#    print(input[d1][d2])
      universe[0][d1][d2] = input[d1][d2]
      universe4d[0][0][d1][d2] = input[d1][d2]

def check_neighbors(i, j, k, d):
  dimx, dimy, dimz = np.shape(d)
  occupied = 0
  for (x, y, z) in dirs:
    di = i+x
    dj = j+y
    dk = k+z
    if x == 0 and y == 0 and z == 0:
      continue
    elif di < 0 or dj < 0 or dk < 0:
      continue
    elif di >= dimx or dj >= dimy or dk >= dimz:
      continue
    elif d[di][dj][dk] == 1:
      occupied += 1
  return(occupied)


def check_neighbors4d(i, j, k, l, d):
  dimx, dimy, dimz, dimw = np.shape(d)
  occupied = 0
  for (x, y, z, w) in dirs4d:
    di = i+x
    dj = j+y
    dk = k+z
    dl = l+w
    if x == 0 and y == 0 and z == 0 and w == 0:
      continue
    elif di < 0 or dj < 0 or dk < 0 or dl < 0:
      continue
    elif di >= dimx or dj >= dimy or dk >= dimz or dl >= dimw:
      continue
    elif d[di][dj][dk][dl] == 1:
      occupied += 1
  return(occupied)


def run_rounds(newuniverse, r=6):
  for i in range(r):
    newuniverse=np.pad(newuniverse, (1,1))
    x, y, z = np.shape(newuniverse)
    altuniverse=np.zeros(np.shape(newuniverse))
    for ux in range(x):
      for uy in range(y):
        for uz in range(z):
          neighbors = check_neighbors(ux, uy, uz, newuniverse)
          if newuniverse[ux][uy][uz] == 1: 
            if neighbors in (2,3):
              altuniverse[ux][uy][uz] = 1
            else:
              altuniverse[ux][uy][uz] = 0
          elif neighbors == 3:
            altuniverse[ux][uy][uz] = 1
          else:
            altuniverse[ux][uy][uz] = 0
    newuniverse=altuniverse
  return(int(sum(newuniverse.flatten())))

def run_rounds4d(newuniverse, r=6):
  for i in range(r):
    newuniverse=np.pad(newuniverse, (1,1))
    x, y, z, w = np.shape(newuniverse)
    altuniverse=np.zeros(np.shape(newuniverse))
    for ux in range(x):
      for uy in range(y):
        for uz in range(z):
          for uw in range(w):
            neighbors = check_neighbors(ux, uy, uz, uw, newuniverse)
            if newuniverse[ux][uy][uz][uw] == 1: 
              if neighbors in (2,3):
                altuniverse[ux][uy][uz][uw] = 1
              else:
                altuniverse[ux][uy][uz][uw] = 0
            elif neighbors == 3:
              altuniverse[ux][uy][uz][uw] = 1
            else:
              altuniverse[ux][uy][uz][uw] = 0
    newuniverse=altuniverse
  return(int(sum(newuniverse.flatten())))


part1 = run_rounds(universe)
print(part1)

#part2 = run_rounds4d(universe)
#print(part2)