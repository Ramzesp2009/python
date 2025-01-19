from __future__ import annotations

# from typing import Any, Type, TypeVar


class Geom: pass
class Point2D(Geom):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)



p = Point2D(10, 20)




