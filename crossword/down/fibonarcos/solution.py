# -*- coding: utf-8 -*-

"""
4d. Fibonarcos

Essentially, the approach here is to use a decision tree to exploit
factorization patterns found in the problem space.  It is possible to do a more
naive solution.  Such a naive sol was also attempted and ran within time on the
GSA env, but with not much to spare.  At the time I was under the impression
there might be more hidden test cases (with scarier, bigger values of N), so I
was looking for some way of doing it more quickly.  This odd method is the
result of that worry.  I also tried general counting function approximations
for the group generated by the Fibonacci numbers (actually, the multiplicative
semi-group), but those approximations didn't have nearly the required resolution
for this task.

N.B. this solution contains some pre-computed elements, but these do not make
the problem trivial, rather they provide useful results that allow the
remainder of the method to work.
"""
from collections import defaultdict


def solution(l: int, r: int) -> int:
    """Count the number of non-Fibonacci integers in the given interval.

    N.B. here, this does not mean a Fibonacci *number*, but rather an element
    of the multiplicative semigroup generated by the Fibonacci numbers.

    Args:
        l: The left bound of the interval.
        r: The right bound of the interval.

    Returns:
        The number of integers in the interval which are not Fibonacci integers.

    """
    count = 0
    for n in range(l, r + 1):
        if not is_fib_integer(n):
            count += 1
    return count


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
        l, r = [int(x) for x in f.read().strip().split(' ')]
    return solution(l, r)


# Pre-computation of the first 93 Fibonacci numbers.  This covers up to 10^19,
# which means these are sufficient for the given bounds of the problem.
#
# The following are omitted from this list:
#
#   - 144, since it causes problems with the method, and we are covered since
#     144 = 2^4 * 3^2, and both 2 and 3 are Fibonacci numbers.
#   - 8, with the same reasoning.
#   - The first elements: 1, 1
#
fibs = [
    7540113804746346429, 4660046610375530309, 2880067194370816120,
    1779979416004714189, 1100087778366101931, 679891637638612258,
    420196140727489673, 259695496911122585, 160500643816367088,
    99194853094755497, 61305790721611591, 37889062373143906, 23416728348467685,
    14472334024676221, 8944394323791464, 5527939700884757, 3416454622906707,
    2111485077978050, 1304969544928657, 806515533049393, 498454011879264,
    308061521170129, 190392490709135, 117669030460994, 72723460248141,
    44945570212853, 27777890035288, 17167680177565, 10610209857723,
    6557470319842, 4052739537881, 2504730781961, 1548008755920, 956722026041,
    591286729879, 365435296162, 225851433717, 139583862445, 86267571272,
    53316291173, 32951280099, 20365011074, 12586269025, 7778742049, 4807526976,
    2971215073, 1836311903, 1134903170, 701408733, 433494437, 267914296,
    165580141, 102334155, 63245986, 39088169, 24157817, 14930352, 9227465,
    5702887, 3524578, 2178309, 1346269, 832040, 514229, 317811, 196418, 121393,
    75025, 46368, 28657, 17711, 10946, 6765, 4181, 2584, 1597, 987, 610, 377,
    233, 89, 55, 34, 21, 13, 5, 3, 2
]

# Pre-computation of factorizations of the Fibonacci numbers
fibs_factors = {7540113804746346429: [3, 139, 461, 4969, 28657, 275449],
                4660046610375530309: [13, 13, 233, 741469, 159607993],
                2880067194370816120: [2, 2, 2, 5, 11, 17, 19, 31, 61, 181, 541,
                                      109441],
                1779979416004714189: [1069, 1665088321800481],
                1100087778366101931: [3, 7, 43, 89, 199, 263, 307, 881, 967],
                679891637638612258: [2, 173, 514229, 3821263937],
                420196140727489673: [6709, 144481, 433494437],
                259695496911122585: [5, 1597, 9521, 3415914041],
                160500643816367088: [2, 2, 2, 2, 3, 3, 13, 29, 83, 211, 281,
                                     421, 1427],
                99194853094755497: [99194853094755497],
                61305790721611591: [2789, 59369, 370248451],
                37889062373143906: [2, 17, 53, 109, 2269, 4373, 19441],
                23416728348467685: [3, 5, 7, 11, 41, 47, 1601, 2161, 3041],
                14472334024676221: [157, 92180471494753],
                8944394323791464: [2, 2, 2, 79, 233, 521, 859, 135721],
                5527939700884757: [13, 89, 988681, 4832521],
                3416454622906707: [3, 37, 113, 9349, 29134601],
                2111485077978050: [2, 5, 5, 61, 3001, 230686501],
                1304969544928657: [73, 149, 2221, 54018521],
                806515533049393: [9375829, 86020717],
                498454011879264: [2, 2, 2, 2, 2, 3, 3, 3, 7, 17, 19, 23, 107,
                                  103681], 308061521170129: [6673, 46165371073],
                190392490709135: [5, 11, 13, 29, 71, 911, 141961],
                117669030460994: [2, 137, 829, 18077, 28657],
                72723460248141: [3, 67, 1597, 3571, 63443],
                44945570212853: [269, 116849, 1429913],
                27777890035288: [2, 2, 2, 89, 199, 9901, 19801],
                17167680177565: [5, 233, 14736206161],
                10610209857723: [3, 7, 47, 1087, 2207, 4481],
                6557470319842: [2, 13, 17, 421, 35239681],
                4052739537881: [557, 2417, 3010349],
                2504730781961: [4513, 555003497],
                1548008755920: [2, 2, 2, 2, 3, 3, 5, 11, 31, 41, 61, 2521],
                956722026041: [353, 2710260697],
                591286729879: [59, 19489, 514229],
                365435296162: [2, 37, 113, 797, 54833],
                225851433717: [3, 7, 7, 13, 29, 281, 14503],
                139583862445: [5, 89, 661, 474541],
                86267571272: [2, 2, 2, 17, 19, 53, 109, 5779],
                53316291173: [953, 55945741], 32951280099: [3, 233, 521, 90481],
                20365011074: [2, 1597, 6376021],
                12586269025: [5, 5, 11, 101, 151, 3001],
                7778742049: [13, 97, 6168709],
                4807526976: [2, 2, 2, 2, 2, 2, 3, 3, 7, 23, 47, 1103],
                2971215073: [2971215073], 1836311903: [139, 461, 28657],
                1134903170: [2, 5, 17, 61, 109441],
                701408733: [3, 43, 89, 199, 307], 433494437: [433494437],
                267914296: [2, 2, 2, 13, 29, 211, 421],
                165580141: [2789, 59369], 102334155: [3, 5, 7, 11, 41, 2161],
                63245986: [2, 233, 135721], 39088169: [37, 113, 9349],
                24157817: [73, 149, 2221],
                14930352: [2, 2, 2, 2, 3, 3, 3, 17, 19, 107],
                9227465: [5, 13, 141961], 5702887: [1597, 3571],
                3524578: [2, 89, 19801], 2178309: [3, 7, 47, 2207],
                1346269: [557, 2417], 832040: [2, 2, 2, 5, 11, 31, 61],
                514229: [514229], 317811: [3, 13, 29, 281],
                196418: [2, 17, 53, 109], 121393: [233, 521],
                75025: [5, 5, 3001], 46368: [2, 2, 2, 2, 2, 3, 3, 7, 23],
                28657: [28657], 17711: [89, 199], 10946: [2, 13, 421],
                6765: [3, 5, 11, 41], 4181: [37, 113], 2584: [2, 2, 2, 17, 19],
                1597: [1597], 987: [3, 7, 47], 610: [2, 5, 61], 377: [13, 29],
                233: [233], 89: [89], 55: [5, 11], 34: [2, 17], 21: [3, 7],
                13: [13], 5: [5], 3: [3], 2: [2]}


r_fibs_factors = defaultdict(set)
for n, fs in fibs_factors.items():
    for f in fs:
        r_fibs_factors[f].add(n)


#
# D-TREE ELEMENTS
#
# These are reasonably standard.
#

MAX_DEPTH = 4


class Node:
    pass


class DecisionNode(Node):
    def __init__(self, factor, left, right):
        self.factor = factor
        self.left = left
        self.right = right

    def run(self, n):
        if n % self.factor == 0:
            return self.left.run(n)
        else:
            return self.right.run(n)


class LeafNode(Node):
    def __init__(self, potential_fibonacci_factors):
        self.potential_fibonacci_factors = potential_fibonacci_factors

    def run(self, n):
        return self.potential_fibonacci_factors


def get_tree(fs, visited_factors=[], carried_factors=[], depth=0):
    if depth >= MAX_DEPTH:
        return LeafNode(sorted(set(list(fs) + carried_factors), reverse=True))

    acc = defaultdict(set)
    for f in fs:
        for x in fibs_factors[f]:
            if x not in visited_factors:
                acc[x].add(f)
    # All factors of the remaining fibs in fs have been visited,
    # -> just insert a leaf node
    if len(acc) == 0:
        return LeafNode(fs)
    # tuples = sorted(acc.items(), key=lambda x: abs(len(fs) / 2 - len(x[1])))
    tuples = sorted(acc.items(), key=lambda x: len(x[1]), reverse=True)
    node = tuples[0]
    factor = node[0]
    leftset = fs
    rightset = set(fs) - node[1]
    right_carried = carried_factors
    left_carried = carried_factors
    if factor in fibs:
        left_carried = [factor] + carried_factors
    return DecisionNode(
        factor,
        get_tree(leftset, visited_factors + [factor], left_carried, depth + 1),
        get_tree(rightset, visited_factors + [factor], right_carried, depth + 1)
    )


decision_tree = get_tree(fibs_factors.keys())


#
# FACTORIZATION ELEMENTS
#
# Make use of caching to reduce repetitive workload.
#

fib_factor_cache = {}
fib_integers_cache = {}


def get_fib_factor(n: int):
    """(Try to) find a Fibonacci factor for the given integer.

    Args:
        n: The integer to check.

    Returns:
        The found factor, or None if none found.

    """
    if n in fib_factor_cache:
        return fib_factor_cache[n]
    potential_fibonacci_factors = decision_tree.run(n)
    for f in potential_fibonacci_factors:
        if n >= f and n % f == 0:
            fib_factor_cache[n] = f
            return f
    return None


def is_fib_integer(n: int) -> bool:
    """Check whether a given integer is a Fibonacci integer.

    N.B. here, this does not mean a Fibonacci *number*, but rather an element
    of the multiplicative semigroup generated by the Fibonacci numbers.

    Args:
        n: The integer to check.

    Returns:
        Whether the given integer is a Fibonacci integer.

    """
    current_n = n
    factor = get_fib_factor(current_n)
    temp = []
    while factor is not None:
        current_n = current_n // factor
        if current_n in fib_integers_cache:
            for x in temp:
                fib_integers_cache[x] = fib_integers_cache[current_n]
            return fib_integers_cache[current_n]
        if current_n == 1:
            for x in temp:
                fib_integers_cache[x] = True
            return True
        temp.append(current_n)
        factor = get_fib_factor(current_n)
    for x in temp:
        fib_integers_cache[x] = False
    return False
