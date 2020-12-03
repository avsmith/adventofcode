#!/usr/bin/env python

def reverse(string): 
  string = string[::-1] 
  return string 

f = open("data/input03.txt")
data = f.read()

testdata = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''

orig = data.splitlines()

def trees_hit(slope ,right = 3, down = 1, debug = False):
  trees = 0
  for y in range(0,len(slope),down):
    slopeline = slope[y]
    slopeint = int(reverse(slopeline.replace('#','1').replace('.','0')),2) 
    x = (y//down * right) % len(slopeline)
    pos = slopeint >> x
    trees += pos&1==1

    if(debug):
      if slopeline[x] == '#':
        newline = slopeline[:x] + 'X' + slopeline[x + 1:]
      else:
        newline = slopeline[:x] + 'O' + slopeline[x + 1:]
      print(slopeline, newline)
  return(trees)

print("Part 1 answer:", trees_hit(orig))
print("Part 2 answer:", trees_hit(orig,1,1)* trees_hit(orig,3,1) * trees_hit(orig,5,1)* trees_hit(orig,7,1)* trees_hit(orig,1,2))


