# -*- coding: utf-8 -*-

from . import solution, crossword_solution, get_score
from crossword.across.recreation import crossword_solution as cws_5a


def test_solution() -> None:
    # Given
    assert 4 == solution('abccaa')


def test_get_score() -> None:
    # Mine
    assert 5 == get_score('aacggg')


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 3 == len(this_cws_str)


def test_crossword_solution_matches_brute_force() -> None:
    assert 196 == this_cws


def test_crossword_solution_consistent_w_5a() -> None:
    cws_5a_ = cws_5a()
    if cws_5a_ is not None:
        assert str(cws_5a_)[-1] == this_cws_str[-1]
