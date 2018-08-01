# -*- coding: utf-8 -*-

from . import solution, crossword_solution, is_fib_integer
from crossword.across.cryptic_clue import crossword_solution as cws_7a
from crossword.across.horse_chestnutting import crossword_solution as cws_10a


def test_solution() -> int:
    # Given
    assert 1 == solution(3, 9)  # 7
    # Mine
    assert 0 == solution(3, 6)
    assert 1 == solution(3, 7)  # 7
    assert 1 == solution(3, 8)  # 7
    assert 1 == solution(3, 9)  # 7
    assert 1 == solution(3, 10)  # 7
    assert 2 == solution(3, 11)  # 7, 11
    assert 2 == solution(3, 12)  # 7, 11


def test_is_fib_integer() -> int:
    # Given
    assert is_fib_integer(5)
    assert is_fib_integer(9)
    assert is_fib_integer(10)
    assert is_fib_integer(12)
    assert not is_fib_integer(11)


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> int:
    assert 6 == len(this_cws_str)


def test_crossword_solution_consistent_w_7a() -> int:
    cws_7a_ = cws_7a()
    if cws_7a_ is not None:
        assert str(cws_7a_)[2] == this_cws_str[3]


def test_crossword_solution_consistent_w_10a() -> int:
    # We know this from the form of 10a, which must start with 12
    assert this_cws_str[-1] == '1'
    cws_10a_ = cws_10a()
    if cws_10a_ is not None:
        assert str(cws_10a_)[0] == this_cws_str[-1]
