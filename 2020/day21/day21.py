#!/usr/bin/env python

from collections import defaultdict
import numpy as np
from functools import reduce
#import pprint as pp
import itertools
import os, sys
import copy

f = open(os.path.join(sys.path[0], 'input21.txt'))
input = f.read()

# List to collect menu details
menu = []

for line in input.splitlines():
  foods, ingredients = line.split(" (contains ")
  foods = foods.split(' ')
  ingredients = ingredients[0:-1].split(', ')
  menu.append({'foods': foods, 'ingredients': ingredients})

# Collect all the menu items by allegen
poss_menu_allergens = defaultdict(list)

for item in menu:
  for ingredient in item['ingredients']:
    poss_menu_allergens[ingredient].append(item['foods'])

# Reduce menu items to  those found in all by ingredient
reduced_menu_allegens = defaultdict(list)

for ingredient in poss_menu_allergens:
  overlap = list(reduce(lambda i, j: i & j, (set(x) for x in poss_menu_allergens[ingredient])))
  reduced_menu_allegens[ingredient] = overlap
  
# NOTE: This reduced list is not 1:1, but expecting that in part 2
# Seeing part2: YUP!!!!

# List of all menu items (allowing repeats)
all_menu_items = list(itertools.chain.from_iterable([x['foods'] for x in menu ]))
# List of all menu items with allergens
allergen_menu_items = list(itertools.chain.from_iterable([v for v in reduced_menu_allegens.values() ]))

part1 = sum(np.logical_not(np.isin(all_menu_items, allergen_menu_items)))
print(f'part1 answer: {part1}')

# Part 2 reduce menu items to allergens 1:1

menu_possibilities = copy.deepcopy(reduced_menu_allegens)

def find_allergens(menu_possibilities):
  menu_stuff  = list(itertools.chain.from_iterable([v for v in menu_possibilities.values() ]))
  while len(menu_stuff) > len(menu_possibilities):
    known_allergens = []
    for item in menu_possibilities:
      if len(menu_possibilities[item]) == 1:
        known_allergens.extend(menu_possibilities[item])
    for known in known_allergens:
      for k in menu_possibilities:
        if len(menu_possibilities[k]) > 1:
          try:
            menu_list = menu_possibilities[k]
            menu_list.remove(known)
            menu_possibilities[k] =  menu_list
          except ValueError:
            pass
    menu_stuff  = list(itertools.chain.from_iterable([v for v in menu_possibilities.values() ]))
  return(menu_possibilities)
    

find_allergens(menu_possibilities)

part2 = ','.join([menu_possibilities[k][0] for k in sorted(menu_possibilities)])
print(f'part2 answer: {part2}')
