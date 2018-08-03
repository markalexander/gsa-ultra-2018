# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.down.q1d import crossword_solution as cws_1d
from crossword.down.q4d import crossword_solution as cws_4d
from crossword.down.q6d import crossword_solution as cws_6d
from crossword.down.q8d import crossword_solution as cws_8d


def test_solution():
    sol = solution()
    assert 8 == len(str(sol))


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len():
    assert 8 == len(this_cws_str)


def test_crossword_solution_consistent_w_1d():
    cws_1d_ = cws_1d()
    if cws_1d_ is not None:
        assert str(cws_1d_)[5] == this_cws_str[0]


def test_crossword_solution_consistent_w_4d():
    cws_4d_ = cws_4d()
    if cws_4d_ is not None:
        assert str(cws_4d_)[3] == this_cws_str[2]


def test_crossword_solution_consistent_w_6d():
    cws_6d_ = cws_6d()
    if cws_6d_ is not None:
        assert str(cws_6d_)[1] == this_cws_str[4]


def test_crossword_solution_consistent_w_8d():
    cws_8d_ = cws_8d()
    if cws_8d_ is not None:
        assert str(cws_8d_)[0] == this_cws_str[-1]

