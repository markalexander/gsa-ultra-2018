# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.across.q7a import crossword_solution as cws_7a


def test_solution() -> None:
    # Given
    assert 2 == solution(3, ((1, 2),))
    assert 2 == solution(3, ((2, 3),))
    # [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    assert 6 == solution(3, ((1, 2), (2, 3)))


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 9 == len(this_cws_str)


def test_crossword_solution_consistent_w_7a() -> None:
    cws_7a_ = cws_7a()
    if cws_7a_ is not None:
        assert str(cws_7a_)[0] == this_cws_str[5]
