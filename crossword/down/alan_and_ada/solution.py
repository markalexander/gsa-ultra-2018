# -*- coding: utf-8 -*-

"""
6d. Alan and Ada

The method here is simple but requires a bit of analysis of the given algorithm.
In fact the given algo is just Kahn's algorithm for topological ordering.  The
reasoning of the solution is given below.

I did also try a Monte-Carlo/sampling-esque approach where I just ran trials
until I got a match, but some of the required events are *so* rare that this is
not really reasonable on the GSA env (or in general).
"""

from collections import defaultdict
from itertools import product


def solution(t) -> int:
    """Calculate the solution for problem 6d.

    Args:
        t: The tuple.

    Returns:
        The solution.

    """
    total = 0
    for i in range(len(t)):
        total += (2**i) * f(*t[i])
    return total % (10**9 + 7)


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    return solution((
        (2, ((1, 2),), (1,)),
        (2, ((1, 2),), (2,)),
        (3, ((1, 2),), (3,)),
        (3, ((1, 2), (1, 3)), (1,)),
        (3, ((1, 2), (2, 3)), (2, 3)),
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 6, 3)),
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 6, 3, 1)),
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 2, 3, 1)),
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 2, 5)),
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (1,)),
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 2, 6, 3, 1)),
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 5))
    ))


def can_nodes_be_kahn_active_set(n, edges, nodes) -> bool:
    """Determine whether the given set of nodes could ever be the active/open
    node set of the Khan topological ordering algo for the given graph.

    Args:
        n:     The number of nodes in the graph.
        edges: The directed edges of the DAG.
        nodes: The 'target' nodes.

    Returns:
        Whether or not this is the case.

    """
    # Convert graph to a more amenable form for path-finding
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)

    # For each pair of target nodes
    for u, v in filter(lambda x: x[0] > x[1], product(nodes, repeat=2)):
        # Two nodes can be the active set together iff there is no directed
        # path between them
        if get_path_between_nodes(g, u, v) or get_path_between_nodes(g, v, u):
            return False

    # Now, we know the active set could at some point contain all the target
    # nodes.  The question becomes could it contain *only* those nodes.
    # However, any open node can be removed at random, and this will only be
    # replaced with another if a node it was connected to now has an in_deg of
    # 0.  But then this new node becomes another open node that can be also be
    # randomly removed, and so it is always possible (even if unlikely) that all
    # are eventually removed *but* the target nodes.
    return True


def get_path_between_nodes(graph, start, end, path=None):
    """Find *any* path between two given nodes of the graph.

    Args:
        graph: The graph, in dict form.
        start: Start node.
        end:   End node.
        path:  Current path for recursive calling.

    Returns:
        The path between the nodes, or None if none exists.

    """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = get_path_between_nodes(graph, node, end, path)
            if new_path:
                return new_path
    return None


def f(*args, **kwargs) -> int:
    """Utility function, defined as f is in the problem statement.

    Args:
        *args:    Args to pass to can_nodes_be_khan_active_set()
        **kwargs: Keyword args to pass to can_nodes_be_khan_active_set()

    Returns:

    """
    return int(can_nodes_be_kahn_active_set(*args, **kwargs))

