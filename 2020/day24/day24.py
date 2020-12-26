#!/usr/bin/env python

import re
import os, sys
from collections import defaultdict

movere = re.compile(r'(e|se|sw|w|nw|ne)')

testinput = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''

f = open(os.path.join(sys.path[0], 'input24.txt'))
input = f.read()

starttiles = defaultdict(lambda:1)

for line in testinput.splitlines():
  pos = 0+0j
  moves = movere.findall(line)
  for move in moves:
    if move == 'e':
      pos += 1
    elif move == 'se':
      pos += 1-1j
    elif move == 'sw':
      pos += 0-1j
    elif move == 'w':
      pos += -1
    elif move == 'nw':
      pos += -1+1j
    elif move == 'ne':
      pos += 1j
  starttiles[pos] *= -1


print(abs(sum([x for x in starttiles.values() if x == -1 ])))

#for part2

dirs = [1, 1-1j, 0-1j, -1, -1+1j, 1j]
seedtiles = [pos for pos, x in starttiles.items() if x == -1 ]


def find_neighbors(pos):
  neighbors = []
  for dir in dirs:
    neighbors.append(pos + dir)
  return(neighbors)

def flip_tiles(positions):
  checktiles = set(positions)
  newtiles = []
  for pos in set(positions):
    checktiles.update(find_neighbors(pos))
  for tile in set(checktiles):
    blacks = [pos for pos in find_neighbors(tile) if pos in set(positions)]
    if tile in set(positions) and len(blacks) > 0 and len(blacks) < 3:
      newtiles.append(tile)
    elif tile not in set(positions) and len(blacks) == 2:
      newtiles.append(tile)
  return(newtiles)

r1 = flip_tiles(seedtiles)
r2 = flip_tiles(r1)
r3 = flip_tiles(r2)
print(len(r1))
print(len(r2))
print(len(r3))

#print(len(flip_tiles(seedtiles)))
  
  


# plotting used to work out a bug (urrgghhh)
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

fig, ax = plt.subplots(1)

def convert_vert(x,y):
  vcoord = 2. * np.sin(np.radians(60)) * (2 * y  + x) /3.
  return(vcoord)

for point in seedtiles:
  x = point.real
  y = convert_vert(point.real, point.imag)
  #print(x,y)
  hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
    orientation=np.radians(30), alpha=0.2, edgecolor='k')
  ax.add_patch(hex)
    # Also add a text label
  ax.text(x, y+0.2, 'X', ha='center', va='center', size=20)

# Also add scatter points in hexagon centres
ax.scatter([point.real for point in starttiles if starttiles[point] == -1 ], [convert_vert(point.real, point.imag) for point in starttiles if starttiles[point] == -1], c='blue', alpha=0.5)

#plt.show()