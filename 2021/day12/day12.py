#!/usr/bin/env python

from collections import defaultdict

input = """by-TW
start-TW
fw-end
QZ-end
JH-by
ka-start
ka-by
end-JH
QZ-cv
vg-TI
by-fw
QZ-by
JH-ka
JH-vg
vg-fw
TW-cv
QZ-vg
ka-TW
ka-QZ
JH-fw
vg-hu
cv-start
by-cv
ka-cv
"""

graph = defaultdict(list)

# For part2
def nonduplicated_smalls(list):
    lowers = [x for x in list if x.islower()]
    if len(lowers) == len(set(lowers)):
        return True
    return False


# based on https://tuxbyte.blogspot.com/2018/07/find-all-existing-paths-in-graph-from.html
def find_paths(graph, start, end, part2=False, path=[]):
    path = path + [start]
    # Reachd end return path
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if (
            node not in path
            # Tweak for part 1 solution
            # Allows revisiting big caves (uppercase)
            or node.isupper()
            # Tweak for part 2 solution
            # Allows one small cave to be revisited
            or (
                part2
                and nonduplicated_smalls(path)
                and node != "start"
                and node != "end"
            )
        ):
            new_paths = find_paths(graph, node, end, part2, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


for line in input.splitlines():
    start, end = line.split("-")
    graph[start].append(end)
    graph[end].append(start)

print("Part 1:", len(find_paths(graph, "start", "end")))
print("Part 2:", len(find_paths(graph, "start", "end", True)))
