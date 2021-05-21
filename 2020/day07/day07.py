#!/usr/bin/env python

import os, sys
import re

# import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

f = open(os.path.join(sys.path[0], "input07.txt"))
input = f.read()

test_input = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

input_list = test_input.splitlines()

contains_bags_re = re.compile("(\w+ \w+) bags contain (\d+) (\w+ \w+) bag")
empty_bags_re = re.compile("(\w+ \w+) bags contain no other bags")
inside_bags_re = re.compile("(\d+) (\w+ \w+) bag")

bag_graph = nx.MultiDiGraph()

for bag_rule in input_list:
    # print(bag_rule)
    # 	print(bag_rule)
    empty_bags_match = empty_bags_re.match(bag_rule)
    contains_bags_match = contains_bags_re.match(bag_rule)
    if empty_bags_match:
        bag = empty_bags_match.group(1)
        bag_graph.add_node(bag)
    elif contains_bags_match:
        (outside_bag, number_bags, first_inside_bag) = contains_bags_match.groups()

        for inside_bag in inside_bags_re.finditer(bag_rule):
            (number_bags, inside_bag_name) = inside_bag.groups()
            #     print(inside_bag_name, "number", number_bags)
            bag_graph.add_edge(outside_bag, inside_bag_name, weight=int(number_bags))

bags_with_shiny_gold = 0

parent_bags = [e[0] for e in bag_graph.out_edges()]
child_bags = [e[1] for e in bag_graph.out_edges()]

for bag in list(bag_graph):
    #  print(bag)
    if bag == "shiny gold":
        continue
    try:
        bag_path_to_gold = nx.shortest_path(bag_graph, source=bag, target="shiny gold")
    except nx.exception.NetworkXNoPath:
        True
    else:
        bags_with_shiny_gold += 1

print(f"There are {bags_with_shiny_gold} bags than could contain a shiny gold bag")

parent_bags = [e[0] for e in bag_graph.out_edges()]
child_bags = [e[1] for e in bag_graph.out_edges()]

print(parent_bags)
print(child_bags)

terminal_bags = np.setdiff1d(child_bags, parent_bags)


def score_path(path):
    score = path[0]
    for i in range(1, len(path)):
        more_bags = np.prod(path[0:i])
        print(more_bags)
        print("b", score)
        score += more_bags
        print("a", score)
    print(score)


for bag in terminal_bags:
    print(bag)
    path_weights = []
    try:
        bag_path_from_gold = nx.shortest_path(
            bag_graph, source="shiny gold", target=bag
        )
    except nx.exception.NetworkXNoPath:
        True
    else:
        for i in range(len(bag_path_from_gold) - 1):
            path_weights.append(
                nx.path_weight(
                    bag_graph,
                    [bag_path_from_gold[i], bag_path_from_gold[i + 1]],
                    "weight",
                )
            )
    print(np.prod(path_weights))
