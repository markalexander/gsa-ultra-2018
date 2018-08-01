# -*- coding: utf-8 -*-

"""
11d. Squared away

Naive method, but runs quite quickly regardless.  Definitely possible to use
caching here but there's not much need.
"""


def solution(a: int) -> int:
    """Get the number of almost-square integers in the interval [10, a].

    This could benefit from a limited-memory lookup/cache since we will be
    repeatedly checking certain values for parts of the sequence e.g. 140, 141,
    142, 143, 144, ... would all require us to check whether 14 is square.
    There's no real need here because the upper bound on the problem size is
    quite small, and this executes in ~2 s even on the limited web env for
    input at the upper bound.  But in theory, for larger n, it would be useful.

    Args:
        a: The end point of the range.

    Returns:
        The number of almost-square integers in the given range.
    """
    count = 0
    for s in range(10, a + 1):
        if is_almost_square(s):
            count += 1
    return count


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    return solution(1234)


def is_square(s: int) -> bool:
    """Check whether an integer is square.

    Args:
        s: The integer to check.

    Returns:
        Whether the integer is square.

    """
    # Special cases
    if s == 0:
        return True
    elif s < 0:
        return False
    # Gen. method
    a, b = 1, s
    while a + 1 < b:
        mp = (a + b) // 2
        if mp ** 2 < s:
            a = mp
        else:
            b = mp
    return s == a ** 2 or s == (a + 1) ** 2


def is_almost_square(s: int) -> bool:
    """Check whether an integer is almost-square.

    Args:
        s: The integer to check.

    Returns:
        Whether the integer is almost-square.

    """
    s = str(s)
    for i in range(len(s)):
        n = int(s[:i] + s[i + 1:])
        if is_square(n):
            return True
    return False
