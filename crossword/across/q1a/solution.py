# -*- coding: utf-8 -*-

"""
1a. Hello world
"""


def solution(a: int, b: int) -> int:
    """Find the sum of two integers.

    Args:
        a: The first integers.
        b: The second integer.

    Returns:
        The sum of the two integers.

    """
    return a + b


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    return solution(5432, 3333)
