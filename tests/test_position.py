import sys

sys.path.insert(0, "/home/bjw/maze")

import pytest
from maze import position


@pytest.fixture
def initial_position():
    """Returns an initial position"""
    return position.Position(2, 4)


@pytest.fixture
def another_position():
    """Returns an initial position"""
    return position.Position(1, 4)


def test_position_coords(initial_position):
    assert initial_position.coords() == (2, 4)


def test_position_coords_rev(initial_position):
    assert initial_position.coords(reverse=True) == (4, 2)


def test_position_add(initial_position, another_position):
    assert (initial_position + another_position).coords() == (3, 8)


def test_position_sub(initial_position, another_position):
    assert (initial_position - another_position).coords() == (1, 0)


def test_position_mul(initial_position):
    assert (initial_position * 2).coords() == (4, 8)


@pytest.mark.parametrize(
    "divisor,expected",
    [
        (1, (2, 4)),
        (2, (1, 2)),
        (3, (1, 1)),
        (4, (1, 1)),
        (5, (0, 1)),
    ],
)
def test_position_div(initial_position, divisor, expected):
    assert (initial_position / divisor).coords() == expected
