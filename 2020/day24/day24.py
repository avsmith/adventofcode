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

for line in input.splitlines():
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

def flip_tiles(blacktiles,n):
  for i in range(n):
    checktiles = set(blacktiles)
    newtiles = []
    for pos in blacktiles:
      checktiles.update(find_neighbors(pos))
    for tile in set(checktiles):
      numneighbors = sum(n in blacktiles for n in find_neighbors(tile))
      if tile in blacktiles:
        if numneighbors in (1,2):
          newtiles.append(tile)
      elif tile not in blacktiles:
        if numneighbors == 2:
            newtiles.append(tile)
#    if (i+1) % 10 == 0:
#      print(i+1, len(newtiles))
    blacktiles=newtiles
    
  return(positions)

r100 = flip_tiles(seedtiles, 100)
print(len(r100))

