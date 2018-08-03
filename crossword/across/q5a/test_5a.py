# -*- coding: utf-8 -*-

from . import solution, crossword_solution
from crossword.down.q2d import crossword_solution as cws_2d
from crossword.down.q3d import crossword_solution as cws_3d


def test_solution() -> None:
    # Given
    assert 2 == solution('xyxy', 'xyy')
    # Mine
    assert 1 == solution('', '')
    assert 1 == solution('a', 'a')
    assert 2 == solution('aa', 'a')
    assert 1 == solution('a', 'aa')
    assert 5 == solution('aaaaaaaaaa', 'aba')
    assert 6 == solution('aaaaaaaaaaa', 'aba')
    assert 3 == solution('bigdogbigbig', 'bigdog')
    assert 9 == solution('123456789', '987654321')
    assert 2 == solution('12x34', 'x1234')
    assert 2 == solution('x1234', '12x34')
    assert 3 == solution('aefghopqrstuvwxyzijklmnbcd',
                         'abcdefghijklmnopqrstuvwxyz')


# Crossword solution tests

this_cws = crossword_solution()
this_cws_str = str(this_cws)


def test_crossword_solution_len() -> None:
    assert 5 == len(this_cws_str)


def test_crossword_solution_consistent_w_2d() -> None:
    cws_2d_ = cws_2d()
    if cws_2d_ is not None:
        assert str(cws_2d_)[2] == this_cws_str[2]


def test_crossword_solution_consistent_w_3d() -> None:
    cws_3d_ = cws_3d()
    if cws_3d_ is not None:
        assert str(cws_3d_)[-1] == this_cws_str[-1]
