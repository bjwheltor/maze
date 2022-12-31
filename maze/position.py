from typing import Tuple


class Position:
    """Represents a Position location or a movement vector"""

    def __init__(self, x: int, y: int) -> None:
        """
        Args:
            x
                x-coordinate
            y
                y-coordinate
        """
        self.x = x
        self.y = y

    def coords(self, reverse: bool = False) -> Tuple[int, int]:
        """
        Return position as a tuple

        Args:
            reverse:
                True is coordinate order to be reversed, i.e. (y, x) rather then (x, y)

        Returns
            Position as a tuple
        """
        if reverse:
            return (self.y, self.x)
        else:
            return (self.x, self.y)

    def __add__(self, other: "Position") -> "Position":
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    def __sub__(self, other: "Position") -> "Position":
        x = self.x - other.x
        y = self.y - other.y
        return Position(x, y)

    def __mul__(self, multiplier: int) -> "Position":
        x = self.x * multiplier

        y = self.y * multiplier
        return Position(x, y)

    def __truediv__(self, divisor: int) -> "Position":
        x = (self.x + divisor // 2) // divisor
        y = (self.y + divisor // 2) // divisor
        return Position(x, y)

    def __repr__(self) -> str:
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}"


# ===============================
# Some tests in isolation
# ===============================
if __name__ == "__main__":

    pos = Position(2, 3)
    print(pos)
    print(pos.coords())
    reverse = True
    print(pos.coords(reverse))
    pos2 = Position(1, 4)
    print(pos2)
    print(pos - pos2)
    multiplier = 20
    pos3 = pos2 * multiplier
    print(pos3)
    divisor = 15
    pos4 = pos3 / divisor
    print(pos4)
