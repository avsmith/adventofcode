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


def part1(lines: list[int], top: int) -> int:
    matrix = parse_matrix(lines)
    pairs = closest_pairs(matrix, top)
    connected = find_connections(pairs)
    groups = find_groups(connected)
    lengths = sorted((len(g) for g in groups), reverse=True)
    return math.prod(lengths[0:3])


def main():
    text = Path("input08.txt").read_text()
    lines = text.splitlines()
    print("Part1:", part1(lines, 1000))


if __name__ == "__main__":
    debug = False
    main()
