import sys

sys.path.insert(0, "/home/bjw/maze")

import pytest
from maze import maze, position


@pytest.fixture
def initial_maze():
    """Returns an initial maze with room set"""
    initial_maze = maze.Maze(position.Position(5, 3))
    initial_maze.set_room(position.Position(3, 1), 1, 90)
    return initial_maze


def test_maze_set_room_id(initial_maze):
    assert initial_maze.place[3, 1, 0] == 1


def test_maze_set_room_rot(initial_maze):
    assert initial_maze.place[3, 1, 1] == 90


@pytest.mark.parametrize(
    "rotate, rot",
    [
        (90, 180),
        (180, 270),
        (270, 0),
        (360, 90),
        (-90, 0),
        (-180, 270),
    ],
)
def test_maze_rotate_room(initial_maze, rotate, rot):
    initial_maze.rotate_room(position.Position(3, 1), rotate)
    assert initial_maze.place[3, 1, 1] == rot
