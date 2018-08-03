# -*- coding: utf-8 -*-

"""
1d. Having a ball

Relatively standard graph components approach to this problem.
"""

from collections import defaultdict
from math import factorial


def solution(n: int, c) -> int:
    """Calculate the number of different configurations achievable.

    Args:
        n: The number of boxes.
        c: The allowed swaps.

    Returns:
        The number of configurations, mod 10^9 + 7.

    """
    answer = 1
    for component in graph_components(c):
        answer *= factorial(len(component))
    return answer % (10**9 + 7)


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
    xs = [int(x) for x in lines[1].split(' ')]
    c = list(chunks(xs, 2))
    return solution(n, c)


def graph_components(edges):
    """
    Given a graph as a list of edges, divide the nodes into components.

    Takes a list of pairs of nodes, where the nodes are integers.
    Returns a list of sets of nodes (the components).

    Args:
        edges: Graph edges.

    Returns:
        The components

    """
    adjacency_list = defaultdict(set)

    for v1, v2 in edges:
        adjacency_list[v1].add(v2)
        adjacency_list[v2].add(v1)

    vertices = set(adjacency_list.keys())

    # A list of sets
    components = []

    # While the vertex set is not empty
    while vertices:
        # Pop a vertex off the set
        start_vertex = vertices.pop()
        component = set()
        to_visit = set([start_vertex])
        while to_visit:
            vertex = to_visit.pop()
            component.add(vertex)
            to_visit = to_visit.union(adjacency_list[vertex] - component)
        components.append(component)
        vertices = vertices - component

    return components


def chunks(l, n):
    """Yield successive n-sized chunks from l.

    From:

        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

    Args:
        l: Index-able object.
        n: Size of desired chunks.

    """
    for i in range(0, len(l), n):
        yield l[i:i + n]
