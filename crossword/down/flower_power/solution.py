# -*- coding: utf-8 -*-

"""
2d. Flower power

Reasonably naive method.  Makes use of some bounds to prune possible candidates.
Runs a bit slow.  Could be better with caching, but it still runs in the given
time.
"""


def solution(s: str) -> int:
    """Count the number of super-colorful subsequences in a flower sequence.

    Args:
        s: The flower sequence (a string of Y, R, B)

    Returns:
        The number of super-colorful subsequences in the sequence (+ 10000)

    """
    count = 0
    for substr in substrings_w_min_length(s):
        if is_super_colorful(substr):
            count += 1
    return 10000 + count


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
        s = f.read().strip()
    return solution(s)


def is_super_colorful(s: str) -> bool:
    """Check whether a given flower sequence is 'super-colorful'

    Args:
        s: The flower sequence to check.

    Returns:
        Whether the sequence is super-colorful.

    """
    for c in ['Y', 'R', 'B']:
        if c not in s:
            return False
    counts = [s.count('Y'), s.count('R'), s.count('B')]
    if len(counts) != len(set(counts)):
        return False
    return True


def substrings_w_min_length(s: str, min_len: int = 6):
    """Get substrings of the given string which are at least the min length.

    This pruning is useful here because there is a lower bound on length for
    super-colorful sequences, by basic combinatorial reasoning:

      - Must be > 3 to meet condition 1.
      - Must be > 4. WLOG let colors be 123. Choose three in unordered set as
        123. Now impossible to choose the last and have unique counts.
      - Must be > 5. Again choose four in unordered set as 1231. Choosing 1 as
        the 5th means 2 and 3 have same count. Choosing 2 or 3 means that 1 will
        have the same count as whichever is chosen.
      - Can be = 6: 122333.

    So min len is 6 and we can ignore all smaller subseqs.

    Args:
        s:       The string.
        min_len: The minimum length.

    Returns:
        All such substrings.

    """
    str_len = len(s)
    for i in range(str_len):
        for j in range(i + min_len - 1, str_len):
            yield s[i:j + 1]
