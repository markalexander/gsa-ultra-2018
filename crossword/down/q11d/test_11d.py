# -*- coding: utf-8 -*-

import pytest
from . import solution, crossword_solution, is_square, is_almost_square
from crossword.across.horse_chestnutting import crossword_solution as cws_10a


def test_solution() -> None:
    # Mine
    # 10 <= s <= 11:
    # 10, 11
    assert 2 == solution(11)
    # 10 <= s <= 25:
    # 10, ..., 19, 20, 21, 24
    assert 13 == solution(25)
    # 10 <= s <= 51:
    # 10, ..., 19, 20, 21, 24, 29, 30, 31, 34, 39, 40, ..., 49, 50, 51
    assert 30 == solution(51)


def test_is_square() -> None:
    # Mine
    assert is_square(0)
    assert is_square(1)
    assert not is_square(2)


def test_is_almost_square() -> None:
    # Given
    assert is_almost_square(1231)
    assert is_almost_square(20)
    assert is_almost_square(200)
    assert not is_almost_square(1254)
    # Mine
    # General almost-squares
    for s in range(10000):
        sq = str(s**2)
        for j in range(len(sq)):
            assert is_almost_square(int(sq[:j] + str(1) + sq[j:]))
    for s in range(10, 20):
        assert is_almost_square(s)
    # General non-almost-squares
    assert not is_almost_square(22)
    assert not is_almost_square(99567)
    # Doesn't make sense for n < 10
    with pytest.raises(ValueError):
        assert not is_almost_square(1)


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert len(str(this_cws)) == 3


def test_crossword_solution_consistent_w_10a() -> None:
    # We know this from the form of 10a, which must start with 12
    assert this_cws_str[0] == '2'
    cws_10a_ = cws_10a()
    if cws_10a_ is not None:
        assert this_cws_str[0] == str(cws_10a_)[1]
