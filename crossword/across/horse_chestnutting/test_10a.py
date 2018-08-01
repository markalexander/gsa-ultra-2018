# -*- coding: utf-8 -*-

from random import randint
from . import solution, crossword_solution, AliceBobGame
from crossword.down.fibonarcos import crossword_solution as cws_4d
from crossword.down.squared_away import crossword_solution as cws_11d
from crossword.down.alan_and_ada import crossword_solution as cws_6d


def test_solution() -> None:
    # Given
    assert 1 + 123 == solution((7,), (5,), (6,), (4,), (3,))


def test_game_winner() -> None:
    # Given
    assert 0 == AliceBobGame(7, 5, 6, 4, 3).winner
    # Mine
    # Can never win from 0
    for i in range(1000):
        assert 1 == AliceBobGame(0, randint(2, 1000), randint(2, 1000),
                                 randint(2, 1000), randint(2, 1000)).winner
    # Can always win directly from 1, 2, 3
    for i in range(1000):
        for j in [1, 2, 3]:
            assert 0 == AliceBobGame(j, randint(2, 1000), randint(2, 1000),
                                     randint(2, 1000), randint(2, 1000)).winner
    # Can never win from 4
    for i in range(1000):
        assert 1 == AliceBobGame(4, randint(2, 1000), randint(2, 1000),
                                 randint(2, 1000), randint(2, 1000)).winner
    # Can force Bob to lose from 5 (by e.g. giving him 4)
    assert 0 == AliceBobGame(6, 6, 6, 13, 13).winner
    # Check divisor logic.  Not a real game case but works for this purpose
    for i in range(10, 1000):
        assert 0 == AliceBobGame(i, 1009, 1009, 1, 1).winner
        assert 1 == AliceBobGame(i, 1, 1, 1009, 1009).winner
        assert 1 == AliceBobGame(i, 1, 1, 1, 1).winner


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 3 == len(this_cws_str)


def test_crossword_solution_consistent_w_reasoning() -> None:
    """Max number of games won is 5, min is 0.  Adding these to the 123 means
    answer must start with 12.
    """
    assert '12' == this_cws_str[:2]


def test_crossword_solution_consistent_w_4d() -> None:
    cws_4d_ = cws_4d()
    if cws_4d_ is not None:
        assert str(cws_4d_)[-1] == this_cws_str[0]


def test_crossword_solution_consistent_w_6d() -> None:
    cws_6d_ = cws_6d()
    if cws_6d_ is not None:
        assert str(cws_6d_)[-1] == this_cws_str[-1]


def test_crossword_solution_consistent_w_11d() -> None:
    cws_11d_ = cws_11d()
    if cws_11d_ is not None:
        assert str(cws_11d_)[0] == this_cws_str[1]
