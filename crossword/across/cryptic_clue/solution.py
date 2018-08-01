# -*- coding: utf-8 -*-

"""
7a. A cryptic crossword clue

This was a combination of exhaustive search and constraints based on the other
crossword entries (see `search.py`).  I wasn't sure if 'a word in hex' meant
purely a-f, or also the letter-like numbers 1 (i, l), 5 (s), 7 (t), etc., but
'facade' appeared to fit best regardless.
"""


def solution() -> int:
    """Get the cryptic crossword solution.

    Returns:
        The cryptic crossword solution, in decimal

    """
    word = 'facade'
    return int(word, 16)


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    return solution()
