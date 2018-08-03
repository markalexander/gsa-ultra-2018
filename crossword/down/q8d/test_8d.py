# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.across.q7a import crossword_solution as cws_7a
from crossword.across.q12a import crossword_solution as cws_12a


def test_solution() -> None:
    # Given
    assert 1 == solution(5, 5, (2, 4), (2, 4), 1)
    # Mine
    # 1
    assert 2 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 1)
    assert 2 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 2)
    assert 4 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 3)
    assert 4 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 4)
    assert 5 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 5)
    assert 5 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 6)
    assert 6 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 7)
    assert 12 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 8)
    assert 15 == solution(9, 15, (1, 5, 7, 9), (1, 4, 9, 15), 9)
    # 2
    assert 2 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 1)
    assert 4 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 2)
    assert 5 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 3)
    assert 10 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 4)
    assert 18 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 5)
    assert 20 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 6)
    assert 25 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 7)
    assert 36 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 8)
    assert 45 == solution(19, 23, (4, 10, 20, 22), (5, 8, 13, 19), 9)


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 5 == len(this_cws_str)


def test_crossword_solution_consistent_w_7a() -> None:
    cws_7a_ = cws_7a()
    if cws_7a_ is not None:
        assert str(cws_7a_)[-1] == this_cws_str[0]


def test_crossword_solution_consistent_w_12a() -> None:
    assert 0 == this_cws_str[-1]  # Since 12a is multiplied by 10000
    cws_12a_ = cws_12a()
    if cws_12a_ is not None:
        assert str(cws_12a_)[2] == this_cws_str[-1]
