import pygame
import numpy as np
from typing import Tuple

import sys

sys.path.insert(0, "/home/bjw/maze")
from maze import position


class Maze:
    """
    Represents the state of the maze as numpy.ndarray called place
    which holds all information on the state of each position
    """

    NUMBER_OF_PLACE_ATTRIBUTES = 2
    ROOM = 0  # attribute with identifier of room
    ROTATION = 1  # attribute with rotation clockwise in degrees
    FULLCIRCLE = 360
    UNSET_VALUE = -1

    def __init__(self, dimensions: "Position") -> None:
        """
        Create empty maze

        Args:
            dimensions:
                Dimensions of the maze in rooms
        """
        self.dimensions = dimensions
        self.rect = pygame.Rect((0, 0), dimensions.coords())

        self.place = np.full(
            [self.rect.width, self.rect.height, self.NUMBER_OF_PLACE_ATTRIBUTES],
            self.UNSET_VALUE,
            dtype=int,
            order="F",
        )

    def set_room(self, position: "Position", room: int, rotation: int = 0) -> None:
        """
        Place a room into the maze.
        Set the coordinate to the room identifier and the rotation.

        Args:
            position:
                Position in the maze
            room:
                Identifier of room to be placed
            rotation:
                Rotation of room to be placed (rotation degrees clockwise)
        """
        self.place[position.x, position.y, self.ROOM] = room
        self.place[position.x, position.y, self.ROTATION] = rotation

    def get_room(self, position: "Position") -> Tuple[int, int]:
        """
        Get the room information for a position in the maze.

        Args:
            pos:
                Position in the maze

        Returns:
            A tuple with then room attributes
            (room indentifier and rotation)
        """
        return (
            self.place[position.x, position.y, self.ROOM],
            self.place[position.x, position.y, self.ROTATION],
        )

    def rotate_room(self, position: "Position", rotate: int) -> None:
        """
        Rotate a room on the board at the specified position

        Args:
            position:
                Position in the maze
            rotate:
                Rotation to be applied to room (degrees clockwise)
        """
        self.place[position.x, position.y, self.ROTATION] = (
            self.place[position.x, position.y, self.ROTATION] + rotate
        ) % self.FULLCIRCLE

    def move_rooms(self, room_block_position: pygame.Rect, move: "Position") -> None:
        """
        Move a block of rooms in the maze

        Args:
            room_block_position:
                Positional description of rectangular block of rooms
            move:
                vector of movement for block of roomes
        """
        # store block of rooms to be moved
        block_of_rooms = self.place[
            room_block_position.left : room_block_position.right,
            room_block_position.top : room_block_position.bottom,
            :,
        ].copy()

        # Unset values of block of rooms in the maze
        self.place[
            room_block_position.left : room_block_position.right,
            room_block_position.top : room_block_position.bottom,
            :,
        ] = self.UNSET_VALUE

        moved_room_block_position = room_block_position.move(move.coords())
        clipped_room_block_position = moved_room_block_position.clip(self.rect)

        patch_rect = pygame.Rect(
            0 + clipped_room_block_position.left - moved_room_block_position.left,
            0 + clipped_room_block_position.top - moved_room_block_position.top,
            clipped_room_block_position.width,
            clipped_room_block_position.height,
        )

        self.place[
            clipped_room_block_position.left : clipped_room_block_position.right,
            clipped_room_block_position.top : clipped_room_block_position.bottom,
            :,
        ] = block_of_rooms[
            patch_rect.left : patch_rect.right, patch_rect.top : patch_rect.bottom, :
        ]

    def __str__(self) -> str:
        """Print maze"""
        string = f"\nMaze layout: {self.dimensions.x} x {self.dimensions.y} - ( Room / Rotation )\n\n"
        for y in range(self.dimensions.y):
            for x in range(self.dimensions.x):

                if y == 0:
                    if x == 0:
                        top = " -----"
                        header = "|     "
                    top += "-----------"
                    header += f"|    {x:2d}    "
                    if x == self.dimensions.x - 1:
                        string += top + "\n" + header + "|\n"

                if x == 0:
                    sep = "|-----"
                    row = f"| {y:2d}  "
                sep += "+----------"

                if self.place[x, y, self.ROOM] == self.UNSET_VALUE:
                    room = " -"
                else:
                    room = f"{self.place[x, y, self.ROOM]:2d}"
                if self.place[x, y, self.ROTATION] == self.UNSET_VALUE:
                    rotation = " - "
                else:
                    rotation = f"{self.place[x, y, self.ROTATION]:3d}"
                row += f"| {room} / {rotation} "

                if x == self.dimensions.x - 1:
                    string += sep + "|\n"
                    string += row + "|\n"

        string = string + top
        return string


# ===============================
# Some tests in isolation
# ===============================
if __name__ == "__main__":

    dimensions = position.Position(5, 3)
    maze = Maze(dimensions)
    print(maze)

    maze.set_room(position.Position(3, 1), 1, 90)
    maze.set_room(position.Position(2, 2), 2, 270)
    print(maze)

    room, rotation = maze.get_room(position.Position(3, 1))
    print(f"\nroom: {room}   rotation: {rotation}\n")

    maze.rotate_room(position.Position(3, 1), 90)
    print(maze)

    room_block_position = pygame.Rect(2, 1, 2, 2)
    move = position.Position(-1, -1)
    maze.move_rooms(room_block_position, move)
    print(maze)
