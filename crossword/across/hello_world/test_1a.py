# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.down.having_a_ball import crossword_solution as cws_1d


def test_solution() -> None:
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            assert a + b == solution(a, b)


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 4 == len(this_cws_str)


def test_crossword_solution_consistent_w_1d() -> None:
    cws_1d_ = cws_1d()
    if cws_1d_ is not None:
        assert str(cws_1d_)[0] == this_cws_str[0]
