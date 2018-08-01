# -*- coding: utf-8 -*-

from . import crossword_solution
from crossword.across.mission_demolition import crossword_solution as cws_12a


def test_solution() -> None:
    # No straightforward way to generate test cases here.  Hope for the best.
    pass


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 5 == len(this_cws_str)


def test_crossword_solution_form() -> None:
    # The map is in seconds, but we return milliseconds -> must end in 000
    assert this_cws_str.endswith('000')


def test_crossword_solution_consistent_w_12a() -> None:
    cws_12a_ = cws_12a()
    if cws_12a_ is not None:
        assert str(cws_12a_)[-1] == this_cws_str[-1]
