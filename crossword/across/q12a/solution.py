# -*- coding: utf-8 -*-

"""
12a. Mission: demolition

Naive graph-based approach using strongly connected components.  Could be
optimized a *lot* more (e.g. with Tarjan) but the given bounds make this method
OK.
"""

from collections import defaultdict


def solution(n: int, x, r) -> int:
    """Get the minimum number of triggers required to detonate the explosives.

    In fact returns this value * 10000, per problem statement.

    Args:
        n: The total number of explosives.
        x: The positions of each explosive.
        r: The power of each explosive.

    Returns:
        The minimum number of triggers * 10000 (the cost, perhaps).

    """
    # Degenerate case
    if n == 0:
        return 0

    (adjacency_list, vertices) = explosive_graph(n, x, r)
    components = strongly_connected_components(adjacency_list, vertices)

    required_detonators = 0
    for component in components:
        in_degree = 0
        for other_component in components - set([component]):
            for vertex in other_component:
                if component & adjacency_list[vertex]:
                    in_degree += 1
                    break
        if in_degree == 0:
            required_detonators += 1
    return required_detonators * 10000


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
    x = [int(x) for x in lines[1].split(' ')]
    r = [int(x) for x in lines[2].split(' ')]
    return solution(n, x, r)


def explosive_graph(n, x, r):
    """Get a graph representation of the problem

    Args:
        n: Number of explosives.
        x: Positions
        r: Powers

    Returns:
        The graph in (adjacency_list, vertices) form.

    """
    edges = set()
    for i in range(0, n):
        for j in range(0, n):
            if x[i] - r[i] <= x[j] <= x[i] + r[i]:
                # Detonating i would detonate j
                edges.add((i, j))
    adjacency_list = defaultdict(set)
    vertices = set()
    for v1, v2 in edges:
        adjacency_list[v1].add(v2)
        vertices.add(v1)
        vertices.add(v2)
    return adjacency_list, vertices


def reachable_vertices(adjacency_list, start_vertex):
    reachable = set()
    to_visit = set([start_vertex])
    while to_visit:
        vertex = to_visit.pop()
        reachable.add(vertex)
        to_visit = to_visit.union(adjacency_list[vertex] - reachable)
    return reachable


def strongly_connected_components(adjacency_list, vertices):
    reachability_list = {}
    for vertex in vertices:
        reachability_list[vertex] = reachable_vertices(adjacency_list, vertex)

    components = set()
    while vertices:
        start_vertex = vertices.pop()
        component = set()
        for vertex in reachability_list[start_vertex]:
            if start_vertex in reachability_list[vertex]:
                component.add(vertex)
        vertices = vertices - component
        components.add(frozenset(component))

    return components
