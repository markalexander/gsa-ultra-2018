# -*- coding: utf-8 -*-

from random import randint


for r_max in [10, 100, 10000]:
    # Randomly generated example at the upper bound on n
    n = 200
    x = []
    r = []
    for i in range(200):
        x.append(randint(0, 10000 + 1))
        r.append(randint(1, r_max + 1))
    x = tuple(x)
    r = tuple(r)

    print('n = {}\nx = {}\nr = {}\n\n'.format(n, x, r))
