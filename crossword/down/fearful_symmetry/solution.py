# -*- coding: utf-8 -*-

"""
3d. Fearful symmetry

This one was probably done most poorly.  It was left until the end because it
seemed straightforward enough at first glance, but in fact it's a little
trickier than you might expect.  As such there was only time to implement a
naive solution (that will run way too slowly at the upper bound of problem
size), but there are other methods that may work.

In general, this is a combinatorial optimization problem but there is an issue
with the common optimality condition on subsets (since it's often not true that
score(x) < score(y) for x a subset, or subsequence, of y.  It could perhaps be
considered as a generalized form of the assignment problem.  Or some other
ancestor of that.  Graph methods might be useful.
"""

from collections import Counter


def solution(s: str) -> int:
    """Get the minimum total score for the given string, as described by the
    problem statement.

    Args:
        s: The string.

    Returns:
        The minimum total score.

    """
    return get_min_partitioned_score(s)


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


min_score_cache = {}


def get_min_partitioned_score(s: str) -> int:
    """Get the minimum partitioned score for the given string.

    Args:
        s: The string.

    Returns:
        The minimum partitioned score.

    """
    n = len(s)
    if n == 1:
        return 1
    if s in min_score_cache:
        return min_score_cache[s]
    best_partitioned_score = 999999
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n, 1):
                if k > j > i:
                    this_partition_score = sum(map(
                        get_score, (s[:i], s[i:j], s[j:k], s[k:])))
                    if this_partition_score < best_partitioned_score:
                        best_partitioned_score = this_partition_score
    #                     best_partition = (s[:i], s[i:j], s[j:k], s[k:])
    # # print('{}'.format(best_partition))
    min_score_cache[s] = best_partitioned_score
    return best_partitioned_score


score_cache = {}


def get_score(s: str) -> int:
    """Calculate the score for a given string, i.e. the length of the longest
    palindrome.

    Args:
        s: The string to check.

    Returns:
        The length of the longest palindrome.

    """
    if s not in score_cache:
        if len(s) <= 2:
            return 1
        counter = Counter(s)
        score = 0
        for count in counter.values():
            if count % 2 == 0:
                score += count
            else:
                score += count - 1
        score_cache[s] = score + 1
    return score_cache[s]
