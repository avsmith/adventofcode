#!/usr/bin/env python

f = open("day08.txt")

d = f.read()

x = 25
y = 6

image = [2] * y * x

smallest = int(x * y)
zeros = smallest

for layer in range(int(len(d) / (x * y))):
    layer_string = d[layer * int(x * y) : ((layer + 1) * int(x * y))]
    layer_counts = {i: layer_string.count(i) for i in set(layer_string)}
    if layer_counts["0"] < smallest:
        smallest = layer_counts["0"]
        if smallest < zeros:
            result1 = int(layer_counts["1"] * layer_counts["2"])
            zeros = smallest
    for i in range(len(image)):
        if image[i] == 2:
            image[i] = int(layer_string[i])

print(result1)

for line in range(int(len(image) / x)):
    line_result = ["X" if c == 1 else " " for c in image[line * x : (line + 1) * x]]
    print("".join(line_result))
