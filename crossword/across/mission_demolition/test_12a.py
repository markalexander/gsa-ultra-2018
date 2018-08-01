# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.down.barb_the_builder import crossword_solution as cws_8d
from crossword.down.amazing_mouse import crossword_solution as cws_9d


def test_solution() -> None:
    # Given
    assert 20000 == solution(4, (2, 6, 7, 10), (1, 3, 2, 5))
    # Mine
    assert 50000 == solution(
        10,
        (9, 2, 21, 4, 11, 50, 29, 3, 5, 20),
        (1, 1, 9,  2, 1,  10, 3,  3, 2, 5)
    )  # crossword case, solved by hand
    assert 10000 == solution(
        3,
        (1, 2, 3),
        (1, 2, 2)
    )
    # No explosives
    assert 0 == solution(0, (), ())
    # Only one explosive
    assert 10000 == solution(1, (1,), (1,))
    # Dense linspace with full propagation
    assert 10000 == solution(200, tuple(range(200)), (1,) * 200)
    # Dense linspace with no propagation
    assert 1000000 == solution(100, tuple(range(0, 200, 2)), (1,) * 200)


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 5 == len(this_cws_str)


def test_crossword_solution_form() -> None:
    # Solution multiplied by 10000 -> must end in 0000
    assert this_cws_str.endswith('0000')


def test_crossword_solution_consistent_w_8d() -> None:
    cws_8d_ = cws_8d()
    if cws_8d_ is not None:
        assert str(cws_8d_)[-1] == this_cws_str[2]


def test_crossword_solution_consistent_w_9d() -> None:
    cws_9d_ = cws_9d()
    if cws_9d_ is not None:
        assert str(cws_9d_)[-1] == this_cws_str[-1]
