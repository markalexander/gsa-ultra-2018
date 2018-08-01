# -*- coding: utf-8 -*-

from . import solution, crossword_solution, is_super_colorful
from crossword.across.recreation import crossword_solution as cws_5a
from crossword.across.cryptic_clue import crossword_solution as cws_7a


def test_solution() -> int:
    # (red, blue, red, red, yellow, yellow, red) is super - colourful.
    assert solution('RRB') == 0 + 10000
    assert solution('RRBYY') == 0 + 10000
    assert solution('RBRRYYR') == 3 + 10000  # RBRRYYR, BRRYYR, RBRRYY


def test_is_super_colourful() -> int:
    # Given
    assert not is_super_colorful('RRB')
    assert not is_super_colorful('RRBYY')
    assert is_super_colorful('RBRRYYR')
    # Mine
    assert not is_super_colorful('RRBBYY')
    assert not is_super_colorful('RBBYY')
    assert not is_super_colorful('RBBRRRRRB')
    assert not is_super_colorful('RBYRBYRBYRBYRBY')
    assert is_super_colorful('RBYRBYRBYRBYRBYRBB')


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> int:
    assert 6 == len(this_cws_str)


def test_crossword_solution_consistent_w_5a() -> int:
    cws_5a_ = cws_5a()
    if cws_5a_ is not None:
        assert str(cws_5a_)[2] == this_cws_str[2]


def test_crossword_solution_consistent_w_7a() -> int:
    cws_7a_ = cws_7a()
    if cws_7a_ is not None:
        assert str(cws_7a_)[-2] == this_cws_str[-1]
