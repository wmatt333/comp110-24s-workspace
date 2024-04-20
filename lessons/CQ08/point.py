"""Creates and modifies a point."""

from __future__ import annotations

__author__ = "730544766"


class Point:
    """Assigns a value to Point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Assigns values to the point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Changes the values of the point itself."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creates a new point and then changes that new points values."""
        Point2 = Point(self.x, self.y)
        Point2.x = Point2.x * factor
        Point2.y = Point2.y * factor
        return Point2