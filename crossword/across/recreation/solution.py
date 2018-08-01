# -*- coding: utf-8 -*-

"""
5a. Recreation through recreating

Simple/naive 'cover' method.
"""


from collections import defaultdict


def solution(a, b) -> int:
    """Get the minimum number of copies of `b` required to create `a` through
    concatenation of subsequences of b's characters.

    Args:
        a: The 'target' string.
        b: The 'source' string.

    Returns:
        The minimum number of copies.

    """
    lookup = defaultdict(list)
    for i, c in enumerate(b):
        lookup[c].append(i)
    cover = []
    current = None
    for i, c in enumerate(a):
        if current is None:
            current = (i, lookup[c][0])
        else:
            nj = next((j for j in lookup[c] if j >= current[1]), len(b))
            current = (current[0], nj)            
        if current[1] == len(b):
            cover.append(current)
            current = (i, lookup[c][0]+1)
        else:
            current = (current[0], current[1] + 1)
    cover.append(current)
    return len(cover)


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    import os
    input_f = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'downloadable_input.fixed.txt')
    with open(input_f, 'r') as f:
        lines = f.readlines()
    a = lines[0].strip()
    b = lines[1].strip()
    return solution(a, b)
