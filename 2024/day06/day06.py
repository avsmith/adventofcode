#!/usr/bin/env python

import os
import sys

from collections import defaultdict


test = """....#.....x
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

f = open(os.path.join(sys.path[0], "input06.txt"))
input = f.read()

grid = [[c for c in l] for l in input.splitlines()]

posx = 0
posy = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "^":
            posx = x
            posy = y
            
my = len(grid)
mx = len(grid[0])

direction = "^"
movex = 0
movey = -1

zs = defaultdict(str)

zs[(posx,posy)] = "Z"

def turn(d):
    if d == "^":
        return(">",1,0)
    elif d ==">":
        return("~",0,1)
    elif d == "~":
        return("<",-1,0)
    elif d == "<":
        return("^",0,-1)
    

while posx >= 0 and posx < mx and posy >=0 and posy < my:
    nx = posx + movex
    ny = posy + movey
    
    if nx <0 or nx >= mx or ny <0 or ny >= my:
        break
    elif grid[ny][nx] == "#":
        direction, movex, movey = turn(direction)
    else:
        posx= nx
        posy = ny
        zs[(posx,posy)] = "Z"
    

print(len(zs)) 

