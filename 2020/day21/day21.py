#!/usr/bin/env python

from collections import defaultdict
import numpy as np
from functools import reduce
#import pprint as pp
import itertools
import os, sys

f = open(os.path.join(sys.path[0], 'input21.txt'))
input = f.read()

testinput = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''

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
  
# NOTE: This reduces list is not 1:1, but expecting that in part 2

# List of all menu items (allowing repeats)
all_menu_items = list(itertools.chain.from_iterable([x['foods'] for x in menu ]))
# List of all menu items with allergens
allergen_menu_items = list(itertools.chain.from_iterable([v for v in reduced_menu_allegens.values() ]))

part1 = sum(np.logical_not(np.isin(all_menu_items, allergen_menu_items)))
print(f'part1 answer: {part1}')
