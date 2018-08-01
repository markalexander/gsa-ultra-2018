# -*- coding: utf-8 -*-

"""
9d. Truly a-mazing mouse

Simple shortest path method via Dijkstra.
"""

import heapq
from collections import defaultdict
from itertools import permutations


def solution(n, m) -> int:
    """Determine the minimum completion time (distance/cost) for the given maze.

    Args:
        n: Number of rows and columns in the maze.
        m: The tuple

    Returns:
        The minimum completion time.

    """
    edges = get_edges(n, m)
    waypoints = get_waypoints(n, m)
    best_path = None
    best_path_cost = None
    for visit in map(list, permutations('RGB', 3)):
        cost = sum(map(
            lambda pair:
                dijkstra(edges, waypoints[pair[0]], waypoints[pair[1]])[0],
                zip(['S'] + visit, visit + ['C']))
        )
        if best_path is None or cost < best_path_cost:
            best_path = visit
            best_path_cost = cost
    return best_path_cost * 1000


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    import os
    input_f = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'downloadable_input.txt')
    with open(input_f, 'r') as f:
        lines = f.readlines()
    n = int(lines[0])
    m = tuple(lines[1:])
    return solution(n, m)


def get_edges(n, m):
    edges = []
    for row in range(0, n):
        for col in range(0, n):
            if col < n-1 and m[row][col] != 'W' and m[row][col+1] != 'W':
                edges.append(((row, col), (row, col + 1)))
                edges.append(((row, col + 1), (row, col)))
            if row < n-1 and m[row][col] != 'W' and m[row + 1][col] != 'W':
                edges.append(((row, col), (row+1, col)))
                edges.append(((row + 1, col), (row, col)))
    return edges


def get_waypoints(n, m):
    waypoints = []
    for row in range(0, n):
        for col in range(0, n):
            if m[row][col] in "SRGBC":
                waypoints.append((m[row][col], (row, col)))
    return dict(waypoints)


def dijkstra(edges, f, t):
    """Run Dijkstra on the given graph.

    Standard implementation from https://gist.github.com/kachayev/5990802,
    slightly modified with a default cost of 1.

    Args:
        edges: The edges of the graph.
        f:     From node
        t:     To node.

    Returns:
        The min cost and path.

    """
    g = defaultdict(list)
    for l, r in edges:
        g[l].append((1, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(q, (next, v2, path))
    print('Could not find path', f, t)
    return float("inf")
