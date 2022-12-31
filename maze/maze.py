import numpy as np
from typing import Tuple


class Maze:
    """
    Represents the state of the maze.

    Attributes:
        ew (int):
            East-West or x-dimension of maze
        ns (int):
            North-south or y-dimension of maze
        na (int):
            Number of attributes describing a position in the maze
        place (numpy.ndarray):
            Holds all information on the state of each position
            or place in the maze.
            Has dimensions ...
    """

    def __init__(self, ew, ns):
        """
        Create empty maze

        Args:
            ew (int):
                East-West or x-dimension of maze
            ns (int):
                North-south or y-dimension of maze

        Keyword Args:

        """
        self.ew = ew
        self.ns = ns
        self.na = 2
        self.size = self.ew * self.ns

        self.place = np.zeros([self.ew, self.ns, self.na], dtype=int, order="F")

    def set_room(self, x: int, y: int, room: int, rot: int = 0):
        """
        Place a room into the maze.
        Set the coordinate to the room identifier and the rotation.

        Args:
            x:
                East-West or x-dimension position in maze
            y:
                North-South or y-dimension position in maze
            room:
                Identifier of roon to be placed

        Keyword Args:
            rot:
                Rotation of room to be placed (rotation degrees clockwise)
        """
        self.place[x, y, 0] = room
        self.place[x, y, 1] = rot

    def get_room(self, x: int, y: int):
        """
        Place a room into the maze.
        Set the coordinate to the room identifier and the rotation.

        Args:
            x:
                East-West or x-dimension position in maze
            y:
                North-South or y-dimension position in maze
        """
        return self.place[x, y, 0], self.place[x, y, 1]

    def __str__(self) -> str:
        """Print maze"""
        string = f"\nMaze layout: {self.ew} x {self.ns} - ( Room / Rotation )\n\n"
        for y in range(self.ns):
            for x in range(self.ew):
                if y == 0:
                    if x == 0:
                        top = " -----"
                        header = "|     "
                    top += "-----------"
                    header += f"|    {x:2d}    "
                    if x == self.ew - 1:
                        string += top + "\n" + header + "|\n"
                if x == 0:
                    sep = "|-----"
                    row = f"| {y:2d}  "
                sep += "+----------"
                row += f"| {self.place[x, y, 0]:2d} / {self.place[x, y, 1]:3d} "
                if x == self.ew - 1:
                    string += sep + "|\n"
                    string += row + "|\n"
        string = string + top
        return string


# ===============================
# Some tests in isolation
# ===============================
if __name__ == "__main__":

    ew = 5
    ns = 3
    maze = Maze(ew, ns)
    print(maze)

    maze.set_room(3, 1, 1, 90)
    maze.set_room(2, 2, 2, 270)
    print(maze)

    room, rot = maze.get_room(3, 1)
    print(f"\nroom: {room}   rot: {rot}\n")
