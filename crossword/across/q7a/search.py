# -*- coding: utf-8 -*-

from itertools import product

from crossword.down.q1d.solution import crossword_solution as cws_1d
from crossword.down.q4d.solution import crossword_solution as cws_4d
from crossword.down.q6d.solution import crossword_solution as cws_6d
from crossword.down.q2d.solution import crossword_solution as cws_2d
from crossword.down.q8d.solution import crossword_solution as \
    cws_8d

alpha = ['a', 'b', 'c', 'd', 'e', 'f']


def char(h, pos):
    sol = h()
    if sol is None:
        return None
    else:
        return str(sol)[pos - 1]


# Constraints from existing words in crossword: Across
# (position, value) [1-indexing]
constraints = [
    (1, char(cws_1d, 6)),
    (3, char(cws_4d, 4)),
    (5, char(cws_6d, 2)),
    (7, char(cws_2d, 4)),
    (8, char(cws_8d, 1)),
]


print('Constraints (pos, char):')
print(constraints)


def is_valid(w) -> bool:
    w_dec = int(w, 16)
    w_dec_str = str(w_dec)
    if len(w_dec_str) != 8:
        return False
    for c in constraints:
        if c[1] is not None and w_dec_str[c[0] - 1] != str(c[1]):
            return False
    return True


valid = []
for w in [''.join(c) for c in product(alpha, repeat=6)]:
    if is_valid(w):
        valid.append(w)

print('{:,} valid candidate(s) found'.format(len(valid)))
for word in valid:
    print('{} - {}'.format(int(word, 16), word))
