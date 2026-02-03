#!/usr/bin/env python3

from pathlib import Path
import heapq
import math


def parse_matrix(lines: list[int]):
    return [[int(x) for x in row.split(",")] for row in lines]


def closest_pairs(points, k=10):
    """
    points: list of (x,y,z) floats/ints, length n
    returns: list of (dist, i, j) sorted ascending by dist
    """
    heap = []  # will store (-dist2, i, j) as a max-heap via negative

    n = len(points)
    for i in range(n):
        xi, yi, zi = points[i]
        for j in range(i + 1, n):
            xj, yj, zj = points[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            dist2 = (
                dx * dx + dy * dy + dz * dz
            )  # squared distance is enough for ranking

            if len(heap) < k:
                heapq.heappush(heap, (-dist2, i, j))
            else:
                # heap[0] is the worst (largest dist2) among the kept k
                if dist2 < -heap[0][0]:
                    heapq.heapreplace(heap, (-dist2, i, j))

    result = [(math.sqrt(-d2), i, j) for (d2, i, j) in heap]
    result.sort(key=lambda t: t[0])
    return result


def find_connections(pairs):
    connections = {}

    for _, i, j in pairs:
        if i not in connections:
            connections[i] = []
        if j not in connections:
            connections[j] = []

        connections[i].append(j)
        connections[j].append(i)

    return connections


def find_groups(connections):
    groups = []
    visited = set()

    for start in connections:
        if start in visited:
            continue

        group = []
        todo = [start]
        visited.add(start)

        while todo:
            current = todo.pop()
            group.append(current)

            for neighbor in connections[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    todo.append(neighbor)

        groups.append(group)
    return groups


def part1(lines, top) -> int:
    matrix = parse_matrix(lines)
    pairs = closest_pairs(matrix, top)
    connected = find_connections(pairs)
    groups = find_groups(connected)
    lengths = sorted((len(g) for g in groups), reverse=True)
    return math.prod(lengths[0:3])


class SimpleUF:
    def __init__(self, n):
        # each box starts in its own circuit
        self.parent = list(range(n))
        self.components = n

    def find(self, x):
        # walk up until you reach the circuit leader
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        # already connected
        if ra == rb:
            return False

        # connect rb's circuit into ra's circuit
        self.parent[rb] = ra
        self.components -= 1
        return True


def last_connection_product(points):
    n = len(points)

    # build all edges (distance, i, j)
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
            d2 = dx * dx + dy * dy + dz * dz
            edges.append((d2, i, j))

    edges.sort()

    uf = SimpleUF(n)
    last_i = last_j = None

    for _, i, j in edges:
        if uf.union(i, j):
            last_i, last_j = i, j
            if uf.components == 1:
                break

    return points[last_i][0] * points[last_j][0]


def part2(lines) -> int:
    matrix = parse_matrix(lines)
    last_product = last_connection_product(matrix)
    return last_product


def main():
    text = Path("input08.txt").read_text()
    lines = text.splitlines()
    print("Part1:", part1(lines, 1000))
    print("Part2:", part2(lines))


if __name__ == "__main__":
    debug = False
    main()
