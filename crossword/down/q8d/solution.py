# -*- coding: utf-8 -*-

"""
8d. Barb the builder

The method here is relatively straightforward.  Naive solutions work but fail
(on the GSE env) either due to time or memory constraints (depending on which
naive solution you might use).  Even using heapq to store only the k-best
proved unfruitful.  I also tried a dict-of-counts approach but in the end
this is what worked best.
"""

import heapq
from collections import Counter


def solution(n, m, r, c, k) -> int:
    """Find the area of the k-th smallest room in a given arrangement of walls.

    Args:
        n: The total number of rows.
        m: The total number of columns.
        r: The specification of wall positions on rows.
        c: The specification of wall positions on rows.
        k: The desired ranking of k-th smallest room.

    Returns:
        The area of the k-th smallest room.

    """
    xs = []
    # Add all the non-zero room widths to xs
    last_column_wall = None
    for col in c:
        if last_column_wall is not None and col - last_column_wall - 1 > 0:
            xs.append(col - last_column_wall - 1)
        last_column_wall = col
    ys = []
    # Add all the non-zero room heights to ys
    last_row_wall = None
    for row in r:
        if last_row_wall is not None and row - last_row_wall - 1 > 0:
            ys.append(row - last_row_wall - 1)
        last_row_wall = row
    return aux(xs, ys, k)


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
    n, m = (int(x) for x in lines[0].split(' '))
    r = [int(x) for x in lines[1].split(' ')]
    c = [int(x) for x in lines[2].split(' ')]
    k = int(lines[3])
    return solution(n, m, r, c, k)


def aux(xs, ys, k):
    """Helper function."""
    cxs = Counter(xs)
    cys = Counter(ys)
    xs = sorted(set(xs))
    ys = sorted(set(ys))
    h = []
    heapq.heappush(h, (xs[0] * ys[0], 0, 0))
    while h:
        (area, i, j) = heapq.heappop(h)
        # Remove from k the number of rooms width that height and width
        # using the counters
        k -= cxs[xs[i]] * cys[ys[j]]
        if k <= 0:
            return area
        if j < len(ys) - 1:
            heapq.heappush(h, (xs[i] * ys[j+1], i, j+1))
            if j == 0 and i < len(xs) - 1:
                heapq.heappush(h, (xs[i+1] * ys[0], i+1, 0))
