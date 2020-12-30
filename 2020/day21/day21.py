#!/usr/bin/env python

from collections import defaultdict
import numpy as np
from functools import reduce
import pprint as pp
import itertools


import os, sys

f = open(os.path.join(sys.path[0], 'input21.txt'))
input = f.read()

testinput = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''


allergens = defaultdict(list)
allergens2 = []



for line in input.splitlines():
  foods, ingredients = line.split(" (contains ")
  foods = foods.split(' ')
  ingredients = ingredients[0:-1].split(', ')
  for i in ingredients:
    allergens[i].append(foods)
  allergens2.append({'foods': foods, 'ingredients': ingredients})

overlapped_ingredients = defaultdict(list)

for i in allergens:
  overlap = list(reduce(lambda i, j: i & j, (set(x) for x in allergens[i])))
  overlapped_ingredients[i] = overlap


pp.pprint(overlapped_ingredients)
#all_ingredients = []
real_allergens = list(itertools.chain.from_iterable([overlapped_ingredients[x] for x in overlapped_ingredients ]))



#allfoods = list(itertools.chain.from_iterable([x['foods'] for x in allergens2]))
#allingreds = list(itertools.chain.from_iterable([x['ingredients'] for x in allergens2 ]))



#for i in allingreds:
#  possible = [x['foods'] for x in allergens2 if i in x['ingredients']]
#  print(i, possible)
