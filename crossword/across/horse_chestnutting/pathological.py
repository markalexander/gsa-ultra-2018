# -*- coding: utf-8 -*-

from random import randint

# Number of games can be at most 4

# Initial pile size can be at most 20000

n = 20000

t_n = []
t_a = []
t_b = []
t_x = []
t_y = []


for i in range(5):
    # Keep all near max values
    t_n.append(randint(15000, 20000))
    t_a.append(randint(900, 1000))
    t_b.append(randint(900, 1000))
    t_x.append(randint(900, 1000))
    t_y.append(randint(900, 1000))

print('t_n = {}\nt_a = {}\nt_b = {}\nt_x = {}\nt_y = {}\n'.format(
    tuple(t_n), tuple(t_a), tuple(t_b), tuple(t_x), tuple(t_y)
))
