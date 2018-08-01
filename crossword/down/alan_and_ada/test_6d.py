# -*- coding: utf-8 -*-

from . import solution, crossword_solution, can_nodes_be_kahn_active_set, f
from crossword.across.cryptic_clue import crossword_solution as cws_7a
from crossword.across.horse_chestnutting import crossword_solution as cws_10a


def test_solution() -> None:
    assert 1 == solution((
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 5)),
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 2, 5))
    ))


def test_f() -> None:
    assert 1 == f(5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 5))
    assert 0 == f(5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 2, 5))


def test_checker() -> None:
    # Given
    assert can_nodes_be_kahn_active_set(
        5,
        ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)),
        (1, 5)
    )
    assert not can_nodes_be_kahn_active_set(
        5,
        ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)),
        (1, 2, 5)
    )
    # Mine
    assert can_nodes_be_kahn_active_set(
        5,
        ((1, 3), (1, 2), (2, 3), (3, 4), (5, 4)),
        (1, 5)
    )
    # Empty node set matches because we start with such a set
    assert can_nodes_be_kahn_active_set(
        5,
        ((1, 3), (1, 2), (2, 3), (3, 4), (5, 4)),
        ()
    )


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 4 == len(this_cws_str)


def test_crossword_solution_consistent_w_7a() -> None:
    cws_7a_ = cws_7a()
    if cws_7a_ is not None:
        assert str(cws_7a_)[4] == this_cws_str[1]


def test_crossword_solution_consistent_w_10a() -> None:
    cws_10a_ = cws_10a()
    if cws_10a_ is not None:
        assert str(cws_10a_)[-1] == this_cws_str[-1]
